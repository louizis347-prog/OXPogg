// Função de borda do Supabase: cria UM link do Google Meet por horário de aula e o devolve a quem reservou.
// Fluxo: a página chama POST /functions/v1/live-meet com { booking_id, token }.
//  1) valida a reserva; 2) se o horário ainda não tem link, UMA chamada vence a disputa (live_claim_slot)
//  e cria o evento no Google Agenda com Meet; 3) grava o link no horário; 4) convida o aluno pelo e-mail.
// Todo aluno do mesmo horário recebe exatamente o mesmo link.
//
// Segredos (supabase secrets set ...): GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, GOOGLE_REFRESH_TOKEN,
// GOOGLE_CALENDAR_ID (opcional, padrão "primary"). SUPABASE_URL e SUPABASE_SERVICE_ROLE_KEY já existem na função.

const SB = Deno.env.get("SUPABASE_URL")!;
const KEY = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!;
const CAL = Deno.env.get("GOOGLE_CALENDAR_ID") || "primary";
const cors = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
  "Content-Type": "application/json",
};
const json = (b: unknown, status = 200) => new Response(JSON.stringify(b), { status, headers: cors });

const rest = (path: string, init: RequestInit = {}) =>
  fetch(`${SB}/rest/v1/${path}`, {
    ...init,
    headers: { apikey: KEY, Authorization: `Bearer ${KEY}`, "Content-Type": "application/json", ...(init.headers || {}) },
  });

async function googleToken(): Promise<string> {
  const r = await fetch("https://oauth2.googleapis.com/token", {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({
      client_id: Deno.env.get("GOOGLE_CLIENT_ID")!,
      client_secret: Deno.env.get("GOOGLE_CLIENT_SECRET")!,
      refresh_token: Deno.env.get("GOOGLE_REFRESH_TOKEN")!,
      grant_type: "refresh_token",
    }),
  });
  const j = await r.json();
  if (!j.access_token) throw new Error("google_auth_failed");
  return j.access_token;
}

async function getSlot(id: string) {
  const r = await rest(`live_slots?id=eq.${encodeURIComponent(id)}&select=*`);
  return (await r.json())[0];
}

async function createEvent(slot: any, groupTitle: string, email: string, gtoken: string) {
  const start = new Date(slot.starts_at);
  const end = new Date(start.getTime() + (slot.duration_min || 90) * 60000);
  const r = await fetch(
    `https://www.googleapis.com/calendar/v3/calendars/${encodeURIComponent(CAL)}/events?conferenceDataVersion=1&sendUpdates=all`,
    {
      method: "POST",
      headers: { Authorization: `Bearer ${gtoken}`, "Content-Type": "application/json" },
      body: JSON.stringify({
        summary: `Pogglot · ${groupTitle}`,
        description: "Aula ao vivo em grupo da Pogglot. Use o mesmo link do Google Meet desta reunião.",
        start: { dateTime: start.toISOString(), timeZone: "America/Sao_Paulo" },
        end: { dateTime: end.toISOString(), timeZone: "America/Sao_Paulo" },
        attendees: [{ email }],
        guestsCanInviteOthers: false,
        conferenceData: { createRequest: { requestId: slot.id, conferenceSolutionKey: { type: "hangoutsMeet" } } },
      }),
    },
  );
  const ev = await r.json();
  const url = ev.hangoutLink || ev.conferenceData?.entryPoints?.find((e: any) => e.entryPointType === "video")?.uri;
  if (!url) throw new Error("meet_not_created");
  return { url, eventId: ev.id as string };
}

async function addAttendee(eventId: string, email: string, gtoken: string) {
  const base = `https://www.googleapis.com/calendar/v3/calendars/${encodeURIComponent(CAL)}/events/${eventId}`;
  const h = { Authorization: `Bearer ${gtoken}`, "Content-Type": "application/json" };
  const cur = await (await fetch(base, { headers: h })).json();
  const list: any[] = cur.attendees || [];
  if (list.some((a) => (a.email || "").toLowerCase() === email.toLowerCase())) return;
  await fetch(`${base}?sendUpdates=all`, { method: "PATCH", headers: h, body: JSON.stringify({ attendees: [...list, { email }] }) });
}

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: cors });
  try {
    const { booking_id, token } = await req.json();
    const br = await rest(`live_bookings?id=eq.${encodeURIComponent(booking_id)}&token=eq.${encodeURIComponent(token)}&select=*`);
    const booking = (await br.json())[0];
    if (!booking) return json({ error: "not_found" }, 404);
    let slot = await getSlot(booking.slot_id);
    if (slot.meet_url) {
      // já existe: só garante o convite deste aluno no mesmo evento
      if (slot.event_id) { try { await addAttendee(slot.event_id, booking.email, await googleToken()); } catch (_) { /* o link já vale */ } }
      return json({ meet_url: slot.meet_url });
    }
    const claim = await (await rest("rpc/live_claim_slot", { method: "POST", body: JSON.stringify({ p_slot: slot.id }) })).json();
    if (claim === true) {
      const gr = await (await rest(`live_groups?id=eq.${slot.group_id}&select=title`)).json();
      const g = await googleToken();
      const { url, eventId } = await createEvent(slot, gr[0]?.title || "Aula ao vivo", booking.email, g);
      await rest(`live_slots?id=eq.${encodeURIComponent(slot.id)}&meet_url=is.null`, {
        method: "PATCH", body: JSON.stringify({ meet_url: url, event_id: eventId }),
      });
    } else {
      // outro pedido está criando o link: espera até 12 s
      for (let i = 0; i < 12 && !(slot = await getSlot(booking.slot_id)).meet_url; i++) await new Promise((r) => setTimeout(r, 1000));
    }
    slot = await getSlot(booking.slot_id);
    if (!slot.meet_url) return json({ pending: true }, 202);
    return json({ meet_url: slot.meet_url });
  } catch (e) {
    return json({ error: String((e as Error).message || e) }, 500);
  }
});
