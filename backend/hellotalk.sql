-- Pogglot · extras estilo HelloTalk: reações e "digitando…"
-- Rode uma vez no Supabase: SQL Editor > New query > cole tudo > Run.
-- Sem isto o app continua funcionando: reações e "digitando…" apenas ficam ocultos.

create table if not exists public.reactions (
  msg_id bigint not null references public.messages(id) on delete cascade,
  uid    uuid   not null default auth.uid() references public.profiles(id) on delete cascade,
  emoji  text   not null check (char_length(emoji) between 1 and 8),
  created_at timestamptz not null default now(),
  primary key (msg_id, uid)
);
alter table public.reactions enable row level security;
-- vê reações só de mensagens que você já consegue ver (respeita as regras das conversas privadas)
drop policy if exists reactions_read on public.reactions;
create policy reactions_read on public.reactions for select to authenticated
  using (exists (select 1 from public.messages m where m.id = msg_id));
drop policy if exists reactions_write on public.reactions;
create policy reactions_write on public.reactions for insert to authenticated
  with check (uid = auth.uid() and exists (select 1 from public.messages m where m.id = msg_id));
drop policy if exists reactions_update on public.reactions;
create policy reactions_update on public.reactions for update to authenticated
  using (uid = auth.uid()) with check (uid = auth.uid());
drop policy if exists reactions_delete on public.reactions;
create policy reactions_delete on public.reactions for delete to authenticated using (uid = auth.uid());

create table if not exists public.typing (
  room text not null check (char_length(room) <= 80),
  uid  uuid not null default auth.uid() references public.profiles(id) on delete cascade,
  ts   timestamptz not null default now(),
  primary key (room, uid)
);
alter table public.typing enable row level security;
-- em conversa privada (dm:idA:idB) só os dois participantes enxergam; nas salas, qualquer membro logado
drop policy if exists typing_read on public.typing;
create policy typing_read on public.typing for select to authenticated
  using (room not like 'dm:%' or position(auth.uid()::text in room) > 0);
drop policy if exists typing_ins on public.typing;
create policy typing_ins on public.typing for insert to authenticated
  with check (uid = auth.uid() and (room not like 'dm:%' or position(auth.uid()::text in room) > 0));
drop policy if exists typing_upd on public.typing;
create policy typing_upd on public.typing for update to authenticated
  using (uid = auth.uid()) with check (uid = auth.uid());
drop policy if exists typing_del on public.typing;
create policy typing_del on public.typing for delete to authenticated using (uid = auth.uid());
