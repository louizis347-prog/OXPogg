-- Pogglot · comentários por episódio, turmas (painel de professor) e desafios entre amigos
-- Rode uma vez no Supabase: SQL Editor > New query > cole tudo > Run.
-- Sem isto o app continua funcionando: as telas novas apenas avisam que ainda não estão ativas.
-- Requer a tabela public.profiles (já existente) com as colunas id, name, avatar, xp, streak, eps, ach.

-- ============ comentários por episódio ============
create table if not exists public.episode_comments (
  id         bigint generated always as identity primary key,
  ep         text   not null check (char_length(ep) between 3 and 80),
  uid        uuid   not null default auth.uid() references public.profiles(id) on delete cascade,
  body       text   not null check (char_length(body) between 1 and 800),
  created_at timestamptz not null default now()
);
create index if not exists episode_comments_ep on public.episode_comments (ep, created_at desc);
alter table public.episode_comments enable row level security;
drop policy if exists ec_read on public.episode_comments;
create policy ec_read on public.episode_comments for select to authenticated using (true);
drop policy if exists ec_ins on public.episode_comments;
create policy ec_ins on public.episode_comments for insert to authenticated with check (uid = auth.uid());
drop policy if exists ec_del on public.episode_comments;
create policy ec_del on public.episode_comments for delete to authenticated using (uid = auth.uid());

-- ============ turmas ============
create table if not exists public.classes (
  id         uuid primary key default gen_random_uuid(),
  owner      uuid not null default auth.uid() references public.profiles(id) on delete cascade,
  name       text not null check (char_length(name) between 2 and 60),
  code       text not null unique default upper(substr(md5(random()::text || clock_timestamp()::text), 1, 6)),
  created_at timestamptz not null default now()
);
create table if not exists public.class_members (
  class_id  uuid not null references public.classes(id) on delete cascade,
  uid       uuid not null default auth.uid() references public.profiles(id) on delete cascade,
  joined_at timestamptz not null default now(),
  primary key (class_id, uid)
);
alter table public.classes enable row level security;
alter table public.class_members enable row level security;

create or replace function public.in_class(c uuid) returns boolean
language sql security definer set search_path = public stable as $$
  select exists (select 1 from classes where id = c and owner = auth.uid())
      or exists (select 1 from class_members where class_id = c and uid = auth.uid());
$$;

drop policy if exists classes_read on public.classes;
create policy classes_read on public.classes for select to authenticated using (public.in_class(id));
drop policy if exists classes_ins on public.classes;
create policy classes_ins on public.classes for insert to authenticated with check (owner = auth.uid());
drop policy if exists classes_del on public.classes;
create policy classes_del on public.classes for delete to authenticated using (owner = auth.uid());
drop policy if exists cm_read on public.class_members;
create policy cm_read on public.class_members for select to authenticated using (public.in_class(class_id));
drop policy if exists cm_del on public.class_members;
create policy cm_del on public.class_members for delete to authenticated
  using (uid = auth.uid() or exists (select 1 from classes c where c.id = class_id and c.owner = auth.uid()));

-- entrar numa turma pelo código (o aluno não consegue listar turmas, só entrar com o código)
create or replace function public.join_class(p_code text) returns public.classes
language plpgsql security definer set search_path = public as $$
declare c classes;
begin
  select * into c from classes where code = upper(trim(p_code));
  if not found then raise exception 'Código de turma não encontrado' using errcode = 'P0002'; end if;
  insert into class_members (class_id, uid) values (c.id, auth.uid()) on conflict do nothing;
  return c;
end $$;

-- quadro da turma: dono e membros veem nome, avatar e progresso de todos
create or replace function public.class_roster(p_class uuid)
returns table (uid uuid, name text, avatar text, xp int, streak int, eps jsonb, ach jsonb, is_owner boolean, joined_at timestamptz)
language plpgsql security definer set search_path = public stable as $$
begin
  if not public.in_class(p_class) then raise exception 'Sem acesso a esta turma' using errcode = '42501'; end if;
  return query
    select p.id, p.name, p.avatar, coalesce(p.xp,0)::int, coalesce(p.streak,0)::int, to_jsonb(p.eps), to_jsonb(p.ach),
           (p.id = c.owner), coalesce(m.joined_at, c.created_at)
      from classes c
      join profiles p on p.id = c.owner or p.id in (select cm.uid from class_members cm where cm.class_id = c.id)
      left join class_members m on m.class_id = c.id and m.uid = p.id
     where c.id = p_class
     order by coalesce(p.xp,0) desc;
end $$;

-- ============ desafios entre amigos (quem ganha mais XP no período) ============
create table if not exists public.challenges (
  id         uuid primary key default gen_random_uuid(),
  owner      uuid not null default auth.uid() references public.profiles(id) on delete cascade,
  title      text not null check (char_length(title) between 2 and 60),
  code       text not null unique default upper(substr(md5(random()::text || clock_timestamp()::text), 1, 6)),
  starts_at  timestamptz not null default now(),
  ends_at    timestamptz not null default now() + interval '7 days',
  created_at timestamptz not null default now()
);
create table if not exists public.challenge_members (
  challenge_id uuid not null references public.challenges(id) on delete cascade,
  uid          uuid not null default auth.uid() references public.profiles(id) on delete cascade,
  xp0          int  not null default 0,
  joined_at    timestamptz not null default now(),
  primary key (challenge_id, uid)
);
alter table public.challenges enable row level security;
alter table public.challenge_members enable row level security;

create or replace function public.in_challenge(c uuid) returns boolean
language sql security definer set search_path = public stable as $$
  select exists (select 1 from challenges where id = c and owner = auth.uid())
      or exists (select 1 from challenge_members where challenge_id = c and uid = auth.uid());
$$;
drop policy if exists ch_read on public.challenges;
create policy ch_read on public.challenges for select to authenticated using (public.in_challenge(id));
drop policy if exists ch_del on public.challenges;
create policy ch_del on public.challenges for delete to authenticated using (owner = auth.uid());
drop policy if exists chm_read on public.challenge_members;
create policy chm_read on public.challenge_members for select to authenticated using (public.in_challenge(challenge_id));
drop policy if exists chm_del on public.challenge_members;
create policy chm_del on public.challenge_members for delete to authenticated using (uid = auth.uid());

-- criar o desafio já entra o criador (guarda o XP de partida)
create or replace function public.create_challenge(p_title text, p_days int default 7) returns public.challenges
language plpgsql security definer set search_path = public as $$
declare c challenges;
begin
  insert into challenges (owner, title, ends_at)
    values (auth.uid(), trim(p_title), now() + make_interval(days => greatest(1, least(coalesce(p_days,7), 60)))) returning * into c;
  insert into challenge_members (challenge_id, uid, xp0) values (c.id, auth.uid(), coalesce((select xp from profiles where id = auth.uid()),0));
  return c;
end $$;

create or replace function public.join_challenge(p_code text) returns public.challenges
language plpgsql security definer set search_path = public as $$
declare c challenges;
begin
  select * into c from challenges where code = upper(trim(p_code));
  if not found then raise exception 'Código de desafio não encontrado' using errcode = 'P0002'; end if;
  insert into challenge_members (challenge_id, uid, xp0)
    values (c.id, auth.uid(), coalesce((select xp from profiles where id = auth.uid()),0)) on conflict do nothing;
  return c;
end $$;

create or replace function public.challenge_board(p_challenge uuid)
returns table (uid uuid, name text, avatar text, score int)
language plpgsql security definer set search_path = public stable as $$
begin
  if not public.in_challenge(p_challenge) then raise exception 'Sem acesso a este desafio' using errcode = '42501'; end if;
  return query
    select p.id, p.name, p.avatar, greatest(coalesce(p.xp,0) - m.xp0, 0)::int
      from challenge_members m join profiles p on p.id = m.uid
     where m.challenge_id = p_challenge
     order by 4 desc;
end $$;

grant execute on function public.join_class(text), public.class_roster(uuid), public.create_challenge(text,int),
  public.join_challenge(text), public.challenge_board(uuid) to authenticated;
