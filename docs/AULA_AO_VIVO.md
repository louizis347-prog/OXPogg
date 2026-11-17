# Aula ao vivo: agenda, reservas e link único do Google Meet

A página `aula-ao-vivo.html` mostra os grupos e os horários (em horário de Brasília, com o fuso do aluno ao lado), recebe a reserva e entrega o link do Google Meet. **Todo aluno que reserva o mesmo horário recebe o mesmo link**, e cada horário tem o seu próprio link.

## Grupos e horários (edite aqui)

Arquivo `data/live-schedule.json` (a página lê este arquivo). Hoje:

| Grupo | Dia e horário (Brasília) | Duração |
|---|---|---|
| Inglês para quem mora em Portugal | segunda 17:00 e quarta 17:00 (20:00 em Portugal, no horário de inverno) | 1h30 |
| Português para falantes de espanhol | sábado 11:00 | 1h30 |
| Portuguese for English speakers | quinta 20:00 | 1h30 |

`dow`: 0 = domingo, 1 = segunda … 6 = sábado. A capacidade padrão é 8 alunos por horário.

> Os horários acima são uma sugestão minha. Troque no JSON **e** na tabela `live_group_slots` de `backend/live.sql` (o servidor valida os horários pela tabela; os dois precisam ser iguais).

## Ativar (uma vez)

1. **Banco de dados.** No Supabase, abra o SQL Editor e rode `backend/live.sql`. Ele cria os grupos, os horários, as reservas e as funções `live_book`, `live_link` e `live_claim_slot`. As tabelas não ficam abertas: o público só usa a visão `live_slot_public` e as funções.
2. **Google.** No Google Cloud Console:
   - ative a **Google Calendar API**;
   - crie uma credencial **OAuth (aplicativo da Web)**;
   - obtenha um **refresh token** com o escopo `https://www.googleapis.com/auth/calendar.events`, usando a conta do professor (dá para fazer no OAuth Playground, marcando "Use your own OAuth credentials" e "Access type: offline").
3. **Função de borda.** Com a CLI do Supabase:
   ```
   supabase secrets set GOOGLE_CLIENT_ID=... GOOGLE_CLIENT_SECRET=... GOOGLE_REFRESH_TOKEN=... GOOGLE_CALENDAR_ID=primary
   supabase functions deploy live-meet --no-verify-jwt
   ```
   (`--no-verify-jwt` é necessário porque o app usa a chave `sb_publishable_…`, que não é um JWT.)
4. **Opcional.** Para os horários existirem antes da primeira reserva, agende uma chamada diária a `select live_seed_slots(5);` (pg_cron).

## Como o link é gerado

1. O aluno reserva (`live_book`): a vaga é contada e o horário é criado, se ainda não existir.
2. A página chama a função `live-meet`. **Uma única chamada** ganha a disputa por horário (`live_claim_slot`) e cria o evento no Google Agenda com Meet (`conferenceData.createRequest`, usando o código do horário como `requestId`).
3. O link é gravado no horário. Os próximos alunos do mesmo horário só recebem o link que já existe, e o Google envia o convite para o e-mail de cada um, no mesmo evento.

## Sem a agenda ativada

Enquanto o SQL não for rodado, a página funciona em **modo de demonstração**: aparece um aviso, a reserva fica só no aparelho do visitante e nenhum link é gerado. Ela nunca inventa um link.
