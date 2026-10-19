-- Pogglot · painel do professor mais rico: tarefas da turma e última atividade dos alunos
-- Rode DEPOIS de backend/social.sql (e, para a "última atividade", de backend/sync.sql). Pode rodar mais de uma vez.

-- ============ última atividade (usa user_state.updated_at, que o app atualiza ao sincronizar) ============
drop function if exists public.class_roster(uuid);
create function public.class_roster(p_class uuid)
returns table (uid uuid, name text, avatar text, xp int, streak int, eps jsonb, ach jsonb, is_owner boolean, joined_at timestamptz, last_active timestamptz)
language plpgsql security definer set search_path = public stable as $$
begin
  if not public.in_class(p_class) then raise exception 'Sem acesso a esta turma' using errcode = '42501'; end if;
  return query
    select p.id, p.name, p.avatar, coalesce(p.xp,0)::int, coalesce(p.streak,0)::int, to_jsonb(p.eps), to_jsonb(p.ach),
           (p.id = c.owner), coalesce(m.joined_at, c.created_at),
           (select s.updated_at from public.user_state s where s.uid = p.id)
      from classes c
      join profiles p on p.id = c.owner or p.id in (select cm.uid from class_members cm where cm.class_id = c.id)
      left join class_members m on m.class_id = c.id and m.uid = p.id
     where c.id = p_class
     order by coalesce(p.xp,0) desc;
end $$;
grant execute on function public.class_roster(uuid) to authenticated;

-- ============ tarefas da turma ============
create table if not exists public.class_tasks (
  id         uuid primary key default gen_random_uuid(),
  class_id   uuid not null references public.classes(id) on delete cascade,
  title      text not null check (char_length(title) between 2 and 120),
  kind       text not null default 'free' check (kind in ('free','xp')),
  target     int  not null default 0 check (target >= 0 and target <= 100000),
  due_at     timestamptz,
  created_at timestamptz not null default now()
);
create table if not exists public.class_task_progress (
  task_id uuid not null references public.class_tasks(id) on delete cascade,
  uid     uuid not null default auth.uid() references public.profiles(id) on delete cascade,
  xp0     int  not null default 0,
  done    boolean not null default false,
  done_at timestamptz,
  primary key (task_id, uid)
);
alter table public.class_tasks enable row level security;
alter table public.class_task_progress enable row level security;

create or replace function public.task_in_class(t uuid) returns boolean
language sql security definer set search_path = public stable as $$
  select exists (select 1 from class_tasks k where k.id = t and public.in_class(k.class_id));
$$;

drop policy if exists ct_read on public.class_tasks;
create policy ct_read on public.class_tasks for select to authenticated using (public.in_class(class_id));
drop policy if exists ct_del on public.class_tasks;
create policy ct_del on public.class_tasks for delete to authenticated
  using (exists (select 1 from classes c where c.id = class_id and c.owner = auth.uid()));
drop policy if exists ctp_read on public.class_task_progress;
create policy ctp_read on public.class_task_progress for select to authenticated using (public.task_in_class(task_id));

-- só o professor (dono) cria tarefas; guarda o XP de partida de cada aluno
create or replace function public.create_class_task(p_class uuid, p_title text, p_kind text default 'free', p_target int default 0, p_days int default null)
returns public.class_tasks
language plpgsql security definer set search_path = public as $$
declare t class_tasks;
begin
  if not exists (select 1 from classes where id = p_class and owner = auth.uid()) then
    raise exception 'Só o professor da turma pode criar tarefas' using errcode = '42501';
  end if;
  insert into class_tasks (class_id, title, kind, target, due_at)
    values (p_class, trim(p_title), case when p_kind = 'xp' then 'xp' else 'free' end, greatest(coalesce(p_target,0),0),
            case when p_days is null then null else now() + make_interval(days => greatest(1, least(p_days, 365))) end)
    returning * into t;
  insert into class_task_progress (task_id, uid, xp0)
    select t.id, p.id, coalesce(p.xp,0) from profiles p
     where p.id in (select cm.uid from class_members cm where cm.class_id = p_class)
    on conflict do nothing;
  return t;
end $$;

-- o aluno marca "concluí" nas tarefas livres
create or replace function public.mark_task_done(p_task uuid) returns void
language plpgsql security definer set search_path = public as $$
begin
  if not public.task_in_class(p_task) then raise exception 'Sem acesso a esta tarefa' using errcode = '42501'; end if;
  insert into class_task_progress (task_id, uid, xp0, done, done_at)
    values (p_task, auth.uid(), coalesce((select xp from profiles where id = auth.uid()),0), true, now())
  on conflict (task_id, uid) do update set done = true, done_at = now();
end $$;

-- quadro de tarefas: progresso de cada aluno (alunos novos ganham o XP de partida na primeira consulta)
create or replace function public.class_task_board(p_class uuid)
returns table (task_id uuid, uid uuid, name text, avatar text, progress int, done boolean)
language plpgsql security definer set search_path = public as $$
begin
  if not public.in_class(p_class) then raise exception 'Sem acesso a esta turma' using errcode = '42501'; end if;
  insert into class_task_progress (task_id, uid, xp0)
    select k.id, p.id, coalesce(p.xp,0)
      from class_tasks k
      join profiles p on p.id in (select cm.uid from class_members cm where cm.class_id = p_class)
     where k.class_id = p_class
    on conflict do nothing;
  return query
    select k.id, p.id, p.name, p.avatar,
           case when k.kind = 'xp' then greatest(coalesce(p.xp,0) - g.xp0, 0) else (case when g.done then 1 else 0 end) end::int,
           (g.done or (k.kind = 'xp' and k.target > 0 and greatest(coalesce(p.xp,0) - g.xp0, 0) >= k.target))
      from class_tasks k
      join class_task_progress g on g.task_id = k.id
      join profiles p on p.id = g.uid
     where k.class_id = p_class
     order by k.created_at desc, p.name;
end $$;

grant execute on function public.create_class_task(uuid,text,text,int,int), public.mark_task_done(uuid), public.class_task_board(uuid) to authenticated;
