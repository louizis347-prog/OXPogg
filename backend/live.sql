-- Aulas ao vivo: grupos, horários semanais (horário de Brasília), reservas e link único do Google Meet por horário.
-- Rode no SQL Editor do Supabase. Depois publique a função de borda `live-meet` (backend/functions/live-meet).
-- Mantenha os horários abaixo iguais aos de data/live-schedule.json.

create table if not exists live_groups (
  id text primary key,
  title text not null,
  capacity int not null default 8,
  duration_min int not null default 90
);

create table if not exists live_group_slots (
  group_id text not null references live_groups(id) on delete cascade,
  dow int not null check (dow between 0 and 6),          -- 0 = domingo ... 6 = sábado
  local_time time not null,                                -- horário de Brasília
  primary key (group_id, dow, local_time)
);

create table if not exists live_slots (
  id text primary key,                                     -- ex.: pt-en_20261112
  group_id text not null references live_groups(id),
  starts_at timestamptz not null,
  capacity int not null default 8,
  duration_min int not null default 90,
  meet_url text,                                           -- um único link por horário
  event_id text,
  creating_at timestamptz,
  created_at timestamptz not null default now()
);

create table if not exists live_bookings (
  id uuid primary key default gen_random_uuid(),
  slot_id text not null references live_slots(id) on delete cascade,
  name text not null,
  email text not null,
  whatsapp text,
  token text not null default encode(gen_random_bytes(16), 'hex'),
  created_at timestamptz not null default now()
);
create unique index if not exists live_bookings_one_per_email on live_bookings (slot_id, lower(email));

alter table live_groups enable row level security;
alter table live_group_slots enable row level security;
alter table live_slots enable row level security;
alter table live_bookings enable row level security;
-- sem políticas: ninguém lê as tabelas direto; o acesso é pelas funções e pela view abaixo.

insert into live_groups (id, title, capacity, duration_min) values
  ('en-pt', 'Inglês para quem mora em Portugal', 8, 90),
  ('pt-es', 'Portugués para hablantes de español', 8, 90),
  ('pt-en', 'Portuguese for English speakers', 8, 90)
on conflict (id) do nothing;

insert into live_group_slots (group_id, dow, local_time) values
  ('en-pt', 1, '17:00'), ('en-pt', 3, '17:00'),
  ('pt-es', 6, '11:00'),
  ('pt-en', 4, '20:00')
on conflict do nothing;

-- Cria os horários das próximas semanas (chamada pela reserva e, se quiser, por um agendamento diário).
create or replace function live_seed_slots(p_weeks int default 5) returns void
language plpgsql security definer set search_path = public as $$
declare d date; g record;
begin
  for g in select s.group_id, s.dow, s.local_time, gr.capacity, gr.duration_min
           from live_group_slots s join live_groups gr on gr.id = s.group_id loop
    for d in select generate_series((now() at time zone 'America/Sao_Paulo')::date,
                                    (now() at time zone 'America/Sao_Paulo')::date + p_weeks * 7, interval '1 day')::date loop
      if extract(dow from d) = g.dow then
        insert into live_slots (id, group_id, starts_at, capacity, duration_min)
        values (g.group_id || '_' || to_char(d, 'YYYYMMDD'), g.group_id,
                ((d + g.local_time)::timestamp at time zone 'America/Sao_Paulo'), g.capacity, g.duration_min)
        on conflict (id) do nothing;
      end if;
    end loop;
  end loop;
end $$;

-- Visão pública: só o que é seguro mostrar (vagas e se o link já foi gerado).
create or replace view live_slot_public as
  select s.id, s.group_id, s.starts_at, s.capacity, s.duration_min,
         (select count(*) from live_bookings b where b.slot_id = s.id)::int as booked,
         (s.meet_url is not null) as link_ready
  from live_slots s
  where s.starts_at > now() - interval '3 hours';

-- Reserva uma vaga. Mesmo e-mail no mesmo horário devolve a reserva existente.
create or replace function live_book(p_slot text, p_name text, p_email text, p_whatsapp text default null)
returns json language plpgsql security definer set search_path = public as $$
declare s live_slots; b live_bookings; n int;
begin
  if coalesce(trim(p_name), '') = '' or p_email !~* '^[^@\s]+@[^@\s]+\.[^@\s]+$' then raise exception 'invalid_input'; end if;
  perform live_seed_slots(5);
  select * into s from live_slots where id = p_slot for update;
  if not found then raise exception 'slot_not_found'; end if;
  if s.starts_at < now() + interval '30 minutes' then raise exception 'slot_closed'; end if;
  select * into b from live_bookings where slot_id = s.id and lower(email) = lower(p_email);
  if found then
    return json_build_object('booking_id', b.id, 'token', b.token, 'slot_id', s.id, 'starts_at', s.starts_at,
                             'duration_min', s.duration_min, 'meet_url', s.meet_url, 'already', true);
  end if;
  select count(*) into n from live_bookings where slot_id = s.id;
  if n >= s.capacity then raise exception 'slot_full'; end if;
  insert into live_bookings (slot_id, name, email, whatsapp)
  values (s.id, trim(p_name), trim(p_email), nullif(trim(coalesce(p_whatsapp, '')), '')) returning * into b;
  return json_build_object('booking_id', b.id, 'token', b.token, 'slot_id', s.id, 'starts_at', s.starts_at,
                           'duration_min', s.duration_min, 'meet_url', s.meet_url, 'already', false);
end $$;

-- Consulta uma reserva (com o token recebido) e devolve o link do Meet, se já existir.
create or replace function live_link(p_booking uuid, p_token text) returns json
language plpgsql security definer set search_path = public as $$
declare s live_slots; b live_bookings;
begin
  select * into b from live_bookings where id = p_booking and token = p_token;
  if not found then raise exception 'not_found'; end if;
  select * into s from live_slots where id = b.slot_id;
  return json_build_object('booking_id', b.id, 'slot_id', s.id, 'starts_at', s.starts_at,
                           'duration_min', s.duration_min, 'meet_url', s.meet_url);
end $$;

-- Usada só pela função de borda (service role): reserva o direito de criar o link de um horário.
create or replace function live_claim_slot(p_slot text) returns boolean
language plpgsql security definer set search_path = public as $$
declare r int;
begin
  update live_slots set creating_at = now()
   where id = p_slot and meet_url is null and (creating_at is null or creating_at < now() - interval '90 seconds');
  get diagnostics r = row_count;
  return r > 0;
end $$;

revoke all on function live_claim_slot(text) from public, anon, authenticated;
revoke all on function live_seed_slots(int) from public, anon, authenticated;
grant execute on function live_book(text, text, text, text) to anon, authenticated;
grant execute on function live_link(uuid, text) to anon, authenticated;
grant select on live_slot_public to anon, authenticated;
