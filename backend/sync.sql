-- Pogglot · sincronização completa do progresso entre aparelhos
-- Rode uma vez no Supabase: SQL Editor > New query > cole tudo > Run.
-- Sem isto o app continua funcionando: o progresso apenas fica só neste aparelho.

create table if not exists public.user_state (
  uid        uuid primary key default auth.uid() references public.profiles(id) on delete cascade,
  data       jsonb not null default '{}'::jsonb,
  updated_at timestamptz not null default now()
);
alter table public.user_state enable row level security;

drop policy if exists user_state_read on public.user_state;
create policy user_state_read on public.user_state for select to authenticated using (uid = auth.uid());
drop policy if exists user_state_ins on public.user_state;
create policy user_state_ins on public.user_state for insert to authenticated with check (uid = auth.uid());
drop policy if exists user_state_upd on public.user_state;
create policy user_state_upd on public.user_state for update to authenticated using (uid = auth.uid()) with check (uid = auth.uid());
drop policy if exists user_state_del on public.user_state;
create policy user_state_del on public.user_state for delete to authenticated using (uid = auth.uid());

-- limita o tamanho do estado (2 MB) para evitar abuso
alter table public.user_state drop constraint if exists user_state_size;
alter table public.user_state add constraint user_state_size check (pg_column_size(data) < 2000000);
