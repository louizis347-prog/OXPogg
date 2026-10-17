/* PogCloud - camada de "área de membros" do Pogglot.
 * Dois provedores com a mesma API: 'demo' (localStorage) e 'supabase' (REST).
 * Escolha: window.POGGLOT_CONFIG = {supabaseUrl, supabaseAnonKey}; ausente => demo.
 * JS clássico, sem dependências (ES2019). Erros: Error com mensagem em português e err.code. */
(function (W) {
  'use strict';

  var ROOMS = [
    { id: 'geral', name: 'Geral', emoji: '💬' }, { id: 'en', name: 'English', emoji: '🇺🇸' },
    { id: 'es', name: 'Español', emoji: '🇪🇸' }, { id: 'pt', name: 'Português', emoji: '🇧🇷' },
    { id: 'fr', name: 'Français', emoji: '🇫🇷' }, { id: 'de', name: 'Deutsch', emoji: '🇩🇪' },
    { id: 'it', name: 'Italiano', emoji: '🇮🇹' }, { id: 'cafe', name: 'Café cultural', emoji: '☕' }
  ];

  // ---------- utilidades ----------
  var mem = {}; // fallback quando localStorage falha (modo privado etc.)
  function lsGet(k, d) {
    try { var v = W.localStorage.getItem(k); return v === null ? d : JSON.parse(v); }
    catch (e) { return k in mem ? mem[k] : d; }
  }
  function lsSet(k, v) { try { W.localStorage.setItem(k, JSON.stringify(v)); } catch (e) { mem[k] = v; } }
  function lsDel(k) { delete mem[k]; try { W.localStorage.removeItem(k); } catch (e) { /* ignora */ } }

  // link de convite: ?ref=<id de quem convidou>
  function savedRef() { try { var v = W.localStorage.getItem('pogglot:ref') || ''; return /^[0-9a-f-]{36}$/.test(v) ? v : ''; } catch (e) { return ''; } }
  try { var mref = /[?&]ref=([0-9a-f-]{36})/.exec(W.location && W.location.search || ''); if (mref) W.localStorage.setItem('pogglot:ref', mref[1]); } catch (e) { /* ignora */ }
  function fail(msg, code) { var e = new Error(msg); if (code) e.code = code; return e; }
  function noop() {}
  function rid() { return 'u_' + Math.random().toString(36).slice(2, 10) + Date.now().toString(36).slice(-4); }
  function enc(s) { return encodeURIComponent(s); }
  function str(v, max) { return (v == null ? '' : String(v)).trim().slice(0, max); }
  function langList(a) {
    if (!Array.isArray(a)) return [];
    return a.map(function (x) { return str(x, 8).toLowerCase(); }).filter(Boolean).slice(0, 6);
  }
  function int0(v) { v = Math.floor(Number(v)); return isFinite(v) && v > 0 ? Math.min(v, 1e9) : 0; }
  function sumVals(o) { var t = 0; Object.keys(o || {}).forEach(function (k) { t += int0(o[k]); }); return t; }
  function checkRoom(room) {
    if (typeof room !== 'string' || !/^[A-Za-z0-9:_-]{1,100}$/.test(room)) throw fail('Sala inválida.', 'bad_room');
    return room;
  }
  function checkEmail(email) {
    email = str(email, 200).toLowerCase();
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) throw fail('E-mail inválido.', 'bad_email');
    return email;
  }
  function checkStats(s) {
    s = s || {};
    var eps = {}, ach = {};
    Object.keys(s.eps || {}).forEach(function (k) { if (/^[a-z]{2}$/.test(k)) eps[k] = int0(s.eps[k]); });
    Object.keys(s.ach || {}).forEach(function (k) { if (k.length <= 60) ach[k] = Number(s.ach[k]) || 0; });
    return { xp: int0(s.xp), streak: int0(s.streak), eps: eps, ach: ach };
  }
  function checkProfile(p, requireName) {
    p = p || {};
    var o = {};
    if (p.name !== undefined || requireName) {
      o.name = str(p.name, 40);
      if (!o.name) throw fail('Informe seu nome.', 'bad_name');
    }
    if (p.avatar !== undefined) o.avatar = str(p.avatar, 16);
    if (p.native !== undefined) o.native = str(p.native, 8).toLowerCase();
    if (p.learning !== undefined) o.learning = langList(p.learning);
    if (p.bio !== undefined) o.bio = str(p.bio, 300);
    return o;
  }
  function checkPass(pw) {
    if (typeof pw !== 'string' || pw.length < 6) throw fail('A senha precisa ter pelo menos 6 caracteres.', 'weak_password');
    return pw;
  }
  function pubUser(p, email) {
    return {
      id: p.id, email: email || p.email || '', name: p.name || '', avatar: p.avatar || '',
      native: p.native || '', learning: Array.isArray(p.learning) ? p.learning.slice() : [], bio: p.bio || ''
    };
  }
  // perfil público (com números) a partir de uma linha/objeto
  function pubProfile(r) {
    var o = {
      id: r.id, name: r.name || 'Aluno', avatar: r.avatar || '🙂', native: r.native || '',
      learning: Array.isArray(r.learning) ? r.learning.slice() : [], bio: r.bio || '',
      xp: int0(r.xp), streak: int0(r.streak), eps: r.eps || {}, ach: r.ach || {}
    };
    if (r.demo) o.demo = true;
    return o;
  }
  // monta o ranking: filtra, pontua, ordena e numera
  function rankList(list, lang, by, limit) {
    var rows = list.map(pubProfile);
    if (lang) {
      if (by === 'eps') rows = rows.filter(function (r) { return int0(r.eps[lang]) > 0; });
      else rows = rows.filter(function (r) { return r.learning.indexOf(lang) >= 0; });
    }
    rows.forEach(function (r) {
      r.epsTotal = sumVals(r.eps);
      r.score = by === 'streak' ? r.streak : by === 'eps' ? (lang ? int0(r.eps[lang]) : r.epsTotal) : r.xp;
    });
    rows.sort(function (a, b) { return b.score - a.score || b.xp - a.xp || (a.name < b.name ? -1 : 1); });
    rows = rows.slice(0, Math.max(1, Math.min(limit || 50, 200)));
    rows.forEach(function (r, i) { r.rank = i + 1; });
    return rows;
  }
  function checkText(text) {
    text = typeof text === 'string' ? text.trim() : '';
    if (!text) throw fail('Escreva uma mensagem.', 'empty');
    if (text.length > 1000) throw fail('Mensagem muito longa (máx. 1000 caracteres).', 'too_long');
    return text;
  }
  function peerOf(room, me) {
    var p = room.split(':');
    return p[1] === me ? p[2] : p[1];
  }

  // =====================================================================
  // Provedor DEMO (localStorage, sem rede)
  // =====================================================================
  var K = {
    acc: 'pogglot:demo:accounts', me: 'pogglot:demo:me', seeded: 'pogglot:demo:seeded',
    mem: 'pogglot:demo:members', msgs: 'pogglot:demo:msgs', rep: 'pogglot:demo:reports', blk: 'pogglot:demo:blocks'
  };

  // Hash simples (cyrb53) com sal. NÃO é seguro: serve só para o modo demo local.
  function cyrb(s, seed) {
    var h1 = 0xdeadbeef ^ seed, h2 = 0x41c6ce57 ^ seed;
    for (var i = 0; i < s.length; i++) {
      var ch = s.charCodeAt(i);
      h1 = Math.imul(h1 ^ ch, 2654435761); h2 = Math.imul(h2 ^ ch, 1597334677);
    }
    h1 = Math.imul(h1 ^ (h1 >>> 16), 2246822507) ^ Math.imul(h2 ^ (h2 >>> 13), 3266489909);
    h2 = Math.imul(h2 ^ (h2 >>> 16), 2246822507) ^ Math.imul(h1 ^ (h1 >>> 13), 3266489909);
    return (4294967296 * (2097151 & h2) + (h1 >>> 0)).toString(36);
  }
  function passHash(pw, salt) { salt = salt || Math.random().toString(36).slice(2, 10); return salt + '$' + cyrb(salt + ':' + pw, 7); }
  function passOk(pw, stored) { return passHash(pw, String(stored).split('$')[0]) === stored; }

  var SEED_MEMBERS = [
    { id: 'demo-camila', name: 'Camila Rojas', avatar: '🌻', native: 'es', learning: ['pt', 'en'], bio: 'Chilena em Santiago. Amo música brasileira!', xp: 2840, streak: 21, eps: { en: 14, pt: 6 }, ach: { first: 1, week: 1 } },
    { id: 'demo-mateus', name: 'Mateus Oliveira', avatar: '🎸', native: 'pt', learning: ['en'], bio: 'Músico de Recife, treinando inglês para viajar.', xp: 4120, streak: 45, eps: { en: 22 }, ach: { first: 1, week: 1, month: 1 } },
    { id: 'demo-sofia', name: 'Sofía Herrera', avatar: '🦋', native: 'es', learning: ['pt'], bio: 'Colombiana, professora de espanhol.', xp: 1510, streak: 9, eps: { pt: 11 }, ach: { first: 1 } },
    { id: 'demo-james', name: 'James Carter', avatar: '🏀', native: 'en', learning: ['pt', 'es'], bio: 'From Austin, TX. Learning Portuguese for work.', xp: 3350, streak: 30, eps: { pt: 17, es: 5 }, ach: { first: 1, week: 1, month: 1 } },
    { id: 'demo-lucia', name: 'Lucía Fernández', avatar: '🌙', native: 'es', learning: ['en', 'fr'], bio: 'Argentina. Series com legenda são meu método.', xp: 980, streak: 4, eps: { en: 8, fr: 2 }, ach: { first: 1 } },
    { id: 'demo-beatriz', name: 'Beatriz Santos', avatar: '🍉', native: 'pt', learning: ['es', 'en'], bio: 'Estudante de Letras em Salvador.', xp: 5240, streak: 62, eps: { es: 19, en: 25 }, ach: { first: 1, week: 1, month: 1, hundred: 1 } },
    { id: 'demo-luca', name: 'Luca Moretti', avatar: '🍕', native: 'it', learning: ['en', 'pt'], bio: 'Di Bologna. Cucino e imparo lingue.', xp: 1720, streak: 12, eps: { en: 10, pt: 4 }, ach: { first: 1, week: 1 } },
    { id: 'demo-hannah', name: 'Hannah Weber', avatar: '🚲', native: 'de', learning: ['en', 'es'], bio: 'Aus Hamburg. Fahrrad und Sprachen.', xp: 2210, streak: 17, eps: { en: 13, es: 7 }, ach: { first: 1, week: 1 } },
    { id: 'demo-camille', name: 'Camille Dubois', avatar: '🥐', native: 'fr', learning: ['pt', 'es'], bio: 'Française à Lyon, fan de bossa nova.', xp: 760, streak: 6, eps: { pt: 5, es: 3 }, ach: { first: 1 } },
    { id: 'demo-diego', name: 'Diego Morales', avatar: '🌮', native: 'es', learning: ['en'], bio: 'Mexicano de Guadalajara. Hablo claro y corrijo con cariño.', xp: 1290, streak: 8, eps: { en: 9 }, ach: { first: 1 } },
    { id: 'demo-gabriela', name: 'Gabriela Lima', avatar: '🌴', native: 'pt', learning: ['fr', 'en'], bio: 'Carioca. Quero morar em Paris um dia.', xp: 3010, streak: 27, eps: { fr: 12, en: 15 }, ach: { first: 1, week: 1, month: 1 } },
    { id: 'demo-emma', name: 'Emma Johnson', avatar: '📚', native: 'en', learning: ['de', 'es'], bio: 'Londres. Book club e café.', xp: 5960, streak: 88, eps: { de: 20, es: 24 }, ach: { first: 1, week: 1, month: 1, hundred: 1 } },
    { id: 'demo-valentina', name: 'Valentina Rossi', avatar: '🍋', native: 'it', learning: ['pt'], bio: 'Napoli. Ciao a tutti!', xp: 50, streak: 1, eps: { pt: 1 }, ach: {} },
    { id: 'demo-thiago', name: 'Thiago Almeida', avatar: '⚽', native: 'pt', learning: ['en', 'de'], bio: 'Curitiba. Futebol e idiomas.', xp: 640, streak: 3, eps: { en: 4, de: 1 }, ach: { first: 1 } }
  ];
  // [sala, autor, minutos atrás, texto, índice da msg corrigida]
  var SEED_MSGS = [
    ['geral', 'demo-camila', 200, '¡Hola a todos! Soy de Chile y estoy aprendiendo portugués 😊'],
    ['geral', 'demo-mateus', 190, 'Oi Camila! Bem-vinda! Se quiser praticar português, estou por aqui.'],
    ['geral', 'demo-james', 150, 'Hi everyone! Anyone up for a quick language exchange today?'],
    ['geral', 'demo-beatriz', 140, 'Eu topo, James! Falo português e quero treinar meu inglês.'],
    ['en', 'demo-mateus', 120, 'I goes to the gym every morning.'],
    ['en', 'demo-james', 115, 'Small fix: "I go to the gym every morning." 👍', 4],
    ['en', 'demo-emma', 100, 'Good morning! What are you all reading this week?'],
    ['en', 'demo-beatriz', 95, 'I am reading a short story in English, it is hard but fun.'],
    ['en', 'demo-lucia', 80, 'Yesterday I watch a movie with subtitles.'],
    ['en', 'demo-emma', 75, 'Nice! Just a tiny fix: "Yesterday I watched a movie with subtitles."', 8],
    ['en', 'demo-diego', 60, 'Thanks Emma! Past tense is my enemy 😅'],
    ['es', 'demo-sofia', 180, 'Buenas tardes, ¿alguien quiere practicar español conmigo?'],
    ['es', 'demo-beatriz', 170, '¡Yo! Estoy aprendiendo español. Mi nombre es Beatriz.'],
    ['es', 'demo-sofia', 165, 'Mucho gusto, Beatriz. ¡Tu español ya suena muy bien!'],
    ['es', 'demo-beatriz', 160, 'Ayer yo fui al mercado y compré muchas frutas.'],
    ['es', 'demo-diego', 45, 'Un detalle: en español solemos decir "Ayer fui al mercado" sin el "yo".', 14],
    ['pt', 'demo-mateus', 130, 'Bom dia, pessoal! Hoje o dia está lindo.'],
    ['pt', 'demo-camila', 125, 'Bom dia! Eu gosto muito do clima do Brasil.'],
    ['pt', 'demo-camila', 124, 'Eu estou aprendendo português a dois meses.'],
    ['pt', 'demo-gabriela', 110, 'Quase! O certo é "há dois meses" ou "faz dois meses".', 18],
    ['pt', 'demo-james', 50, 'Obrigado pela dica! Muito útil.'],
    ['cafe', 'demo-luca', 90, 'Qual é o prato típico da sua cidade? Na minha, é a polenta com ragù. 🍲'],
    ['cafe', 'demo-hannah', 70, 'In my city we eat Brezeln with butter for breakfast.'],
    ['cafe', 'demo-camille', 55, 'Chez moi, rien ne vaut un bon croissant avec un café. ☕'],
    ['cafe', 'demo-valentina', 30, 'Che bello! Mi avete fatto venire fame. 😄']
  ];

  var demo = {
    statsDelay: 0, me: null,
    accounts: function () { return lsGet(K.acc, {}); },
    members: function () { return lsGet(K.mem, []); },
    msgs: function () { return lsGet(K.msgs, []); },
    allProfiles: function () {
      var acc = this.accounts();
      return this.members().concat(Object.keys(acc).map(function (e) { return acc[e].profile; }));
    },
    findProfile: function (id) {
      var l = this.allProfiles();
      for (var i = 0; i < l.length; i++) if (l[i].id === id) return l[i];
      return null;
    },
    blocks: function (id) { return (lsGet(K.blk, {})[id]) || []; },
    seed: function () {
      if (lsGet(K.seeded, false)) return;
      var now = Date.now();
      lsSet(K.mem, SEED_MEMBERS.map(function (m) { return Object.assign({ demo: true }, m); }));
      lsSet(K.msgs, SEED_MSGS.map(function (m, i) {
        return { id: i + 1, room: m[0], uid: m[1], text: m[3], ts: now - m[2] * 60000, fixOf: m[4] != null ? m[4] + 1 : null };
      }));
      lsSet(K.seeded, true);
    },
    init: async function () {
      this.seed();
      var id = lsGet(K.me, null), acc = this.accounts();
      this.me = null;
      if (id) Object.keys(acc).forEach(function (e) { if (acc[e].id === id) demo.me = e; });
      if (!this.me) lsDel(K.me);
    },
    cur: function () { return this.me ? this.accounts()[this.me] : null; },
    user: function () { var a = this.cur(); return a ? pubUser(a.profile, this.me) : null; },
    need: function () { var a = this.cur(); if (!a) throw fail('Entre na sua conta para continuar.', 'auth'); return a; },
    login: function (email, a) { this.me = email; lsSet(K.me, a.id); return pubUser(a.profile, email); },
    signUp: async function (d) {
      var email = checkEmail(d.email); checkPass(d.password);
      var p = checkProfile(d, true), acc = this.accounts();
      if (acc[email]) throw fail('Este e-mail já está cadastrado.', 'email_taken');
      var id = rid();
      acc[email] = {
        id: id, pass: passHash(d.password),
        profile: Object.assign({ id: id, avatar: '🙂', native: '', learning: [], bio: '', xp: 0, streak: 0, eps: {}, ach: {} }, p)
      };
      lsSet(K.acc, acc);
      return this.login(email, acc[email]);
    },
    signIn: async function (email, pw) {
      email = str(email, 200).toLowerCase();
      var a = this.accounts()[email];
      if (!a || !passOk(String(pw), a.pass)) throw fail('E-mail ou senha incorretos.', 'bad_credentials');
      return this.login(email, a);
    },
    signOut: async function () { this.me = null; lsDel(K.me); },
    resetPassword: async function (email) { checkEmail(email); },
    updateProfile: async function (p) {
      var a = this.need(), acc = this.accounts();
      Object.assign(acc[this.me].profile, checkProfile(p, false)); lsSet(K.acc, acc);
      return pubUser(acc[this.me].profile, this.me);
    },
    pushStats: async function (s) {
      this.need(); var acc = this.accounts();
      Object.assign(acc[this.me].profile, s); lsSet(K.acc, acc);
    },
    leaderboard: async function (o) { return rankList(this.allProfiles(), o.lang, o.by, o.limit); },
    searchMembers: async function (o) {
      var me = this.need().id, bl = this.blocks(me), q = (o.q || '').toLowerCase();
      var l = this.allProfiles().filter(function (p) {
        return p.id !== me && bl.indexOf(p.id) < 0 &&
          (!q || p.name.toLowerCase().indexOf(q) >= 0) &&
          (!o.native || p.native === o.native) &&
          (!o.learning || (p.learning || []).indexOf(o.learning) >= 0);
      });
      l.sort(function (a, b) { return int0(b.xp) - int0(a.xp); });
      return l.slice(0, o.limit).map(pubProfile);
    },
    getProfile: async function (id) {
      var p = this.findProfile(id);
      if (!p) throw fail('Perfil não encontrado.', 'not_found');
      return pubProfile(p);
    },
    decorate: function (m) {
      var p = this.findProfile(m.uid) || {};
      return { id: m.id, room: m.room, uid: m.uid, name: p.name || 'Aluno', avatar: p.avatar || '🙂', text: m.text, ts: m.ts, fixOf: m.fixOf || null };
    },
    messages: async function (room, o) {
      var me = this.need().id;
      if (room.indexOf('dm:') === 0 && room.split(':').slice(1, 3).indexOf(me) < 0) throw fail('Sem permissão para esta conversa.', 'forbidden');
      var bl = this.blocks(me), self = this;
      var l = this.msgs().filter(function (m) {
        return m.room === room && bl.indexOf(m.uid) < 0 && (o.after == null || m.id > o.after);
      }).sort(function (a, b) { return a.id - b.id; });
      l = o.after == null ? l.slice(-o.limit) : l.slice(0, o.limit);
      return l.map(function (m) { return self.decorate(m); });
    },
    send: async function (room, text, fixOf) {
      var me = this.need().id;
      if (room.indexOf('dm:') === 0 && room.split(':').slice(1, 3).indexOf(me) < 0) throw fail('Sem permissão para esta conversa.', 'forbidden');
      var l = this.msgs(), id = l.reduce(function (n, m) { return Math.max(n, m.id); }, 0) + 1;
      var m = { id: id, room: room, uid: me, text: text, ts: Date.now(), fixOf: fixOf || null };
      l.push(m); lsSet(K.msgs, l);
      return this.decorate(m);
    },
    dmList: async function () {
      var me = this.need().id, bl = this.blocks(me), by = {}, self = this;
      this.msgs().forEach(function (m) {
        if (m.room.indexOf('dm:') !== 0 || m.room.split(':').slice(1, 3).indexOf(me) < 0) return;
        if (!by[m.room] || m.id > by[m.room].id) by[m.room] = m;
      });
      return Object.keys(by).map(function (room) {
        var pid = peerOf(room, me), p = self.findProfile(pid);
        return { room: room, pid: pid, peer: p ? pubProfile(p) : { id: pid, name: 'Aluno', avatar: '🙂', native: '', learning: [] }, last: { text: by[room].text, ts: by[room].ts } };
      }).filter(function (d) { return bl.indexOf(d.pid) < 0; })
        .sort(function (a, b) { return b.last.ts - a.last.ts; })
        .map(function (d) { delete d.pid; return d; });
    },
    report: async function (msgId, reason) {
      var me = this.need().id, l = lsGet(K.rep, []);
      l.push({ id: l.length + 1, msgId: msgId, reporter: me, reason: reason, ts: Date.now() }); lsSet(K.rep, l);
    },
    setBlock: async function (peer, on) {
      var me = this.need().id, all = lsGet(K.blk, {}), l = (all[me] || []).filter(function (x) { return x !== peer; });
      if (on) l.push(peer);
      all[me] = l; lsSet(K.blk, all);
    }
  };

  // =====================================================================
  // Provedor SUPABASE (GoTrue + PostgREST via fetch)
  // =====================================================================
  var SK = 'pogglot:session';
  var PCOLS = 'id,name,avatar,native,learning,bio,xp,streak,eps,ach';
  var sb = {
    statsDelay: 5000, cfg: null, session: null, me: null, refreshing: null, blkCache: null,
    base: function () { return this.cfg.supabaseUrl.replace(/\/+$/, ''); },
    // chamada HTTP crua; token = access_token ou anon key
    raw: async function (method, path, o) {
      o = o || {};
      var h = { apikey: this.cfg.supabaseAnonKey, 'Content-Type': 'application/json' };
      // chaves novas (sb_publishable_...) não são JWT: só vão no cabeçalho apikey
      if (o.token) h.Authorization = 'Bearer ' + o.token; else if (/^eyJ/.test(this.cfg.supabaseAnonKey)) h.Authorization = 'Bearer ' + this.cfg.supabaseAnonKey;
      Object.keys(o.headers || {}).forEach(function (k) { h[k] = o.headers[k]; });
      var res, text;
      try {
        res = await fetch(this.base() + path, { method: method, headers: h, body: o.body !== undefined ? JSON.stringify(o.body) : undefined, keepalive: !!o.keepalive });
        text = await res.text();
      } catch (e) { throw fail('Sem conexão com o servidor. Verifique a internet.', 'network'); }
      var data = null;
      if (text) { try { data = JSON.parse(text); } catch (e) { data = { message: text }; } }
      return { ok: res.ok, status: res.status, data: data };
    },
    persist: function () {
      if (!this.session) return;
      var s = this.session;
      lsSet(SK, { access_token: s.access_token, refresh_token: s.refresh_token, expires_at: s.expires_at, user: s.user, profile: this.me });
    },
    saveSession: function (d) {
      var now = Math.floor(Date.now() / 1000);
      this.session = {
        access_token: d.access_token, refresh_token: d.refresh_token || (this.session && this.session.refresh_token),
        expires_at: d.expires_at || now + (d.expires_in || 3600),
        user: d.user ? { id: d.user.id, email: d.user.email, user_metadata: d.user.user_metadata || {} } : this.session && this.session.user
      };
      this.persist();
    },
    drop: function () { this.session = null; this.me = null; this.blkCache = null; lsDel(SK); emit(null); },
    refresh: function () {
      var self = this;
      if (this.refreshing) return this.refreshing;
      this.refreshing = (async function () {
        var rt = self.session && self.session.refresh_token;
        if (!rt) return false;
        var r = await self.raw('POST', '/auth/v1/token?grant_type=refresh_token', { body: { refresh_token: rt } });
        if (r.ok && r.data && r.data.access_token) { self.saveSession(r.data); return true; }
        if (r.status >= 400 && r.status < 500) { self.drop(); }
        return false;
      })().then(function (v) { self.refreshing = null; return v; }, function (e) { self.refreshing = null; throw e; });
      return this.refreshing;
    },
    // chamada autenticada: renova token ao expirar ou em 401 (uma tentativa)
    api: async function (method, path, o) {
      o = o || {};
      var s = this.session;
      if (!s) throw fail('Entre na sua conta para continuar.', 'auth');
      if (s.expires_at && Date.now() / 1000 > s.expires_at - 30) await this.refresh();
      if (!this.session) throw fail('Sessão expirada. Entre novamente.', 'unauthorized');
      var r = await this.raw(method, path, Object.assign({}, o, { token: this.session.access_token }));
      if (r.status === 401) {
        if (await this.refresh()) r = await this.raw(method, path, Object.assign({}, o, { token: this.session.access_token }));
        else if (!this.session) throw fail('Sessão expirada. Entre novamente.', 'unauthorized');
      }
      if (!r.ok) throw this.httpError(r);
      return r.data;
    },
    httpError: function (r) {
      var d = r.data || {}, m = String(d.message || d.msg || '').toLowerCase();
      if (r.status === 401) return fail('Sessão expirada. Entre novamente.', 'unauthorized');
      if (d.code === 'PGRST205' || d.code === '42P01' || d.code === 'PGRST200') return fail('Banco de dados não configurado (rode o schema.sql).', 'setup');
      if (r.status === 403 || d.code === '42501') return fail('Sem permissão para esta ação.', 'forbidden');
      if (d.code === 'P0001' || d.code === '54000') {
        var mm = String(d.message || '');
        if (mm === 'blocked_content') return fail('Mensagem bloqueada: evite palavrões e ofensas.', 'blocked_content');
        if (mm === 'blocked_links') return fail('Muitos links na mesma mensagem.', 'blocked_links');
        if (mm === 'duplicate') return fail('Você já enviou essa mensagem agora há pouco.', 'duplicate');
        if (mm === 'muted') return fail('Seu chat está pausado por denúncias. Tente de novo mais tarde.', 'muted');
        if (mm === 'rate_limit' || d.code === '54000') return fail('Devagar! Aguarde um segundo entre mensagens.', 'rate_limit');
      }
      if (d.code === '23514') return fail('Dados inválidos (texto muito longo?).', 'invalid');
      if (d.code === '23503' || m.indexOf('foreign key') >= 0) return fail('Perfil ainda não criado. Saia e entre de novo.', 'no_profile');
      if (r.status === 429) return fail('Muitas tentativas. Aguarde um pouco.', 'rate_limit');
      return fail('Erro no servidor (' + r.status + '). Tente de novo.', 'server');
    },
    authError: function (r) {
      var d = r.data || {}, c = String(d.error_code || ''), m = String(d.msg || d.message || d.error_description || d.error || '').toLowerCase();
      if (c === 'invalid_credentials' || /invalid login|invalid_grant/.test(m)) return fail('E-mail ou senha incorretos.', 'bad_credentials');
      if (c === 'email_not_confirmed' || /not confirmed/.test(m)) return fail('Confirme seu e-mail (veja a caixa de entrada) e depois entre.', 'confirm_email');
      if (c === 'user_already_exists' || c === 'email_exists' || /already (registered|exists)/.test(m)) return fail('Este e-mail já está cadastrado.', 'email_taken');
      if (c === 'weak_password' || /password.*(least|short|weak)/.test(m)) return fail('A senha precisa ter pelo menos 6 caracteres.', 'weak_password');
      if (c === 'email_address_invalid' || /invalid.*email|email.*invalid/.test(m)) return fail('E-mail inválido.', 'bad_email');
      if (r.status === 429 || /rate limit/.test(m)) return fail('Muitas tentativas. Aguarde um pouco e tente de novo.', 'rate_limit');
      if (r.status >= 500) return fail('Erro no servidor de login. Tente de novo.', 'server');
      return fail('Não foi possível concluir. Tente de novo.', 'auth_error');
    },
    meta: function (u) {
      var m = (u && u.user_metadata) || {};
      return { id: u.id, email: u.email || '', name: m.name || '', avatar: m.avatar || '', native: m.native || '', learning: Array.isArray(m.learning) ? m.learning : [], bio: '' };
    },
    // garante a linha em profiles (usa user_metadata se ainda não existir)
    ensureProfile: async function () {
      var u = this.session.user, id = u.id, email = u.email;
      var rows = await this.api('GET', '/rest/v1/profiles?select=' + PCOLS + '&id=eq.' + enc(id) + '&limit=1');
      if (!rows.length) {
        var m = this.meta(u);
        rows = await this.api('POST', '/rest/v1/profiles?on_conflict=id', {
          headers: { Prefer: 'resolution=merge-duplicates,return=representation' },
          body: Object.assign({ id: id, name: m.name || (email || 'Aluno').split('@')[0], avatar: m.avatar, native: m.native, learning: m.learning, bio: '' }, /^[0-9a-f-]{36}$/.test(((u.user_metadata || {}).ref) || '') ? { ref_by: u.user_metadata.ref } : {})
        });
      }
      this.me = pubUser(rows[0], email); this.persist();
      return this.me;
    },
    init: async function () {
      var s = lsGet(SK, null);
      if (!s || !s.access_token || !s.user) return;
      this.session = { access_token: s.access_token, refresh_token: s.refresh_token, expires_at: s.expires_at, user: s.user };
      this.me = s.profile || pubUser(this.meta(s.user), s.user.email);
      try {
        if (s.expires_at && Date.now() / 1000 > s.expires_at - 30) await this.refresh();
        if (this.session) await this.ensureProfile();
      } catch (e) { /* offline: segue com o perfil em cache */ }
    },
    user: function () { return this.me ? pubUser(this.me) : null; },
    need: function () { if (!this.session) throw fail('Entre na sua conta para continuar.', 'auth'); return this.session.user; },
    afterLogin: async function (d) {
      this.saveSession(d);
      try { await this.ensureProfile(); } catch (e) { this.me = pubUser(this.meta(this.session.user), this.session.user.email); this.persist(); }
      return this.user();
    },
    signUp: async function (d) {
      var email = checkEmail(d.email); checkPass(d.password);
      var p = checkProfile(d, true);
      var r = await this.raw('POST', '/auth/v1/signup', {
        body: { email: email, password: d.password, data: { name: p.name, avatar: p.avatar || '', native: p.native || '', learning: p.learning || [], ref: savedRef() } }
      });
      if (!r.ok) throw this.authError(r);
      var x = r.data || {};
      if (x.access_token) return this.afterLogin(x);
      // com "Confirm email" ligado não há sessão (identities vazio = e-mail já existe)
      if (Array.isArray(x.identities) && !x.identities.length) throw fail('Este e-mail já está cadastrado.', 'email_taken');
      throw fail('Quase lá! Confirme seu e-mail (veja a caixa de entrada) e depois entre.', 'confirm_email');
    },
    signIn: async function (email, pw) {
      email = checkEmail(email);
      var r = await this.raw('POST', '/auth/v1/token?grant_type=password', { body: { email: email, password: String(pw) } });
      if (!r.ok) throw this.authError(r);
      return this.afterLogin(r.data);
    },
    signOut: async function () {
      if (this.session) { try { await this.raw('POST', '/auth/v1/logout', { token: this.session.access_token }); } catch (e) { /* ignora */ } }
      this.drop();
    },
    resetPassword: async function (email) {
      email = checkEmail(email);
      var r = await this.raw('POST', '/auth/v1/recover', { body: { email: email } });
      if (!r.ok) throw this.authError(r);
    },
    updateProfile: async function (p) {
      var u = this.need(), body = Object.assign({ id: u.id }, checkProfile(p, false), { updated_at: new Date().toISOString() });
      var rows = await this.api('POST', '/rest/v1/profiles?on_conflict=id', { headers: { Prefer: 'resolution=merge-duplicates,return=representation' }, body: body });
      this.me = pubUser(rows[0], u.email); this.persist();
      return this.user();
    },
    pushStats: async function (s) {
      this.need();
      // o servidor valida e limita os números (ver push_stats no schema.sql)
      await this.api('POST', '/rest/v1/rpc/push_stats', {
        keepalive: true,
        body: { p_xp: s.xp, p_streak: s.streak, p_eps: s.eps || {}, p_ach: s.ach || {} }
      });
    },
    leaderboard: async function (o) {
      var q = '/rest/v1/profiles?select=' + PCOLS + '&order=' + (o.by === 'streak' ? 'streak' : 'xp') + '.desc&limit=';
      if (o.by === 'eps') q += 200;
      else { q += Math.min(o.limit, 200); if (o.lang) q += '&learning=' + enc('cs.{' + o.lang + '}'); }
      return rankList(await this.api('GET', q), o.lang, o.by, o.limit);
    },
    blocked: async function (force) {
      var c = this.blkCache;
      if (!force && c && Date.now() - c.t < 60000) return c.ids;
      var u = this.need(), rows = await this.api('GET', '/rest/v1/blocks?select=blocked&blocker=eq.' + enc(u.id));
      this.blkCache = { t: Date.now(), ids: rows.map(function (r) { return r.blocked; }) };
      return this.blkCache.ids;
    },
    searchMembers: async function (o) {
      var u = this.need(), bl = await this.blocked(false);
      var q = '/rest/v1/profiles?select=' + PCOLS + '&id=neq.' + enc(u.id) + '&order=xp.desc&limit=' + (o.limit + bl.length);
      var s = (o.q || '').replace(/[*,()%\\]/g, ' ').trim();
      if (s) q += '&name=' + enc('ilike.*' + s + '*');
      if (o.native) q += '&native=' + enc('eq.' + o.native);
      if (o.learning) q += '&learning=' + enc('cs.{' + o.learning + '}');
      var rows = await this.api('GET', q);
      return rows.filter(function (r) { return bl.indexOf(r.id) < 0; }).slice(0, o.limit).map(pubProfile);
    },
    getProfile: async function (id) {
      var rows = await this.api('GET', '/rest/v1/profiles?select=' + PCOLS + '&id=eq.' + enc(id) + '&limit=1');
      if (!rows.length) throw fail('Perfil não encontrado.', 'not_found');
      return pubProfile(rows[0]);
    },
    msgOut: function (r) {
      var p = r.profiles || {};
      return { id: r.id, room: r.room, uid: r.uid, name: p.name || 'Aluno', avatar: p.avatar || '🙂', text: r.text, ts: Date.parse(r.created_at), fixOf: r.fix_of || null, audio: r.audio || null };
    },
    messages: async function (room, o) {
      this.need();
      var bl = await this.blocked(false), q = '/rest/v1/messages?select=' + enc('*,profiles(name,avatar)') + '&room=' + enc('eq.' + room);
      q += o.after == null ? '&order=id.desc&limit=' + o.limit : '&id=gt.' + enc(o.after) + '&order=id.asc&limit=' + o.limit;
      var rows = await this.api('GET', q);
      if (o.after == null) rows.reverse();
      var self = this;
      return rows.filter(function (r) { return bl.indexOf(r.uid) < 0; }).map(function (r) { return self.msgOut(r); });
    },
    send: async function (room, text, fixOf, audio) {
      var u = this.need(), body = { room: room, uid: u.id, text: text, fix_of: fixOf || null };
      if (audio) body.audio = audio;
      var rows = await this.api('POST', '/rest/v1/messages?select=' + enc('*,profiles(name,avatar)'), {
        headers: { Prefer: 'return=representation' }, body: body
      });
      return this.msgOut(rows[0]);
    },
    dmList: async function () {
      var u = this.need(), bl = await this.blocked(false);
      // RLS já limita a DMs de que o usuário participa
      var rows = await this.api('GET', '/rest/v1/messages?select=id,room,uid,text,created_at&room=' + enc('like.dm:*') + '&order=id.desc&limit=300');
      var by = {}, order = [];
      rows.forEach(function (r) {
        if (r.room.split(':').slice(1, 3).indexOf(u.id) < 0 || by[r.room]) return;
        by[r.room] = r; order.push(r.room);
      });
      order = order.filter(function (room) { return bl.indexOf(peerOf(room, u.id)) < 0; });
      if (!order.length) return [];
      var ids = order.map(function (room) { return peerOf(room, u.id); });
      var ps = await this.api('GET', '/rest/v1/profiles?select=' + PCOLS + '&id=in.' + enc('(' + ids.join(',') + ')'));
      var pm = {};
      ps.forEach(function (p) { pm[p.id] = p; });
      return order.map(function (room) {
        var pid = peerOf(room, u.id), p = pm[pid] ? pubProfile(pm[pid]) : { id: pid, name: 'Aluno', avatar: '🙂', native: '', learning: [] };
        return { room: room, peer: p, last: { text: by[room].text, ts: Date.parse(by[room].created_at) } };
      });
    },
    report: async function (msgId, reason) {
      var u = this.need();
      try { await this.api('POST', '/rest/v1/reports', { headers: { Prefer: 'return=minimal' }, body: { msg_id: msgId, reporter: u.id, reason: reason } }); }
      catch (e) { if (!/\(409\)/.test(e.message || '')) throw e; /* já denunciada: ok */ }
    },
    // ---- voz (Supabase Storage, bucket privado "voice") ----
    token: async function () {
      var s = this.session; if (!s) throw fail('Entre na sua conta para continuar.', 'auth');
      if (s.expires_at && Date.now() / 1000 > s.expires_at - 30) await this.refresh();
      if (!this.session) throw fail('Sessão expirada. Entre novamente.', 'unauthorized');
      return this.session.access_token;
    },
    uploadVoice: async function (blob) {
      var u = this.need(), tk = await this.token(), type = (blob.type || 'audio/webm').split(';')[0];
      var ext = type.indexOf('mp4') >= 0 ? 'm4a' : type.indexOf('ogg') >= 0 ? 'ogg' : type.indexOf('mpeg') >= 0 ? 'mp3' : type.indexOf('wav') >= 0 ? 'wav' : 'webm';
      var path = u.id + '/' + Date.now() + '.' + ext, res;
      try {
        res = await fetch(this.base() + '/storage/v1/object/voice/' + path, { method: 'POST', body: blob,
          headers: { apikey: this.cfg.supabaseAnonKey, Authorization: 'Bearer ' + tk, 'Content-Type': type, 'x-upsert': 'false' } });
      } catch (e) { throw fail('Sem conexão com o servidor. Verifique a internet.', 'network'); }
      if (!res.ok) throw fail(res.status === 413 ? 'Áudio muito grande (máx. 2 MB).' : res.status === 404 ? 'Armazenamento de voz não configurado (rode o extras.sql).' : 'Não foi possível enviar o áudio.', 'upload');
      return path;
    },
    voiceCache: {},
    voiceUrl: async function (path) {
      if (this.voiceCache[path]) return this.voiceCache[path];
      var tk = await this.token(), res;
      try { res = await fetch(this.base() + '/storage/v1/object/authenticated/voice/' + path, { headers: { apikey: this.cfg.supabaseAnonKey, Authorization: 'Bearer ' + tk } }); }
      catch (e) { throw fail('Sem conexão com o servidor. Verifique a internet.', 'network'); }
      if (!res.ok) throw fail('Não foi possível carregar o áudio.', 'audio');
      var url = URL.createObjectURL(await res.blob());
      this.voiceCache[path] = url; return url;
    },
    weekly: async function (o) {
      var d = new Date(), day = (d.getUTCDay() + 6) % 7; d.setUTCDate(d.getUTCDate() - day);
      var week = d.toISOString().slice(0, 10);
      var rows = await this.api('GET', '/rest/v1/weekly_xp?select=' + enc('xp,profiles(' + PCOLS + ')') + '&week=eq.' + week + '&order=xp.desc&limit=' + o.limit);
      return rows.filter(function (r) { return r.profiles; }).map(function (r) { var p = pubProfile(r.profiles); p.week = r.xp; return p; });
    },
    profileStats: async function (id) { return this.api('POST', '/rest/v1/rpc/profile_stats', { body: { p_uid: id } }); },
    logEpisode: function (kind, cid, n, score) {
      if (!this.session) return;
      this.api('POST', '/rest/v1/rpc/log_episode', { keepalive: true, body: { p_kind: kind, p_cid: String(cid), p_n: n | 0, p_score: score || 0 } }).catch(function () { /* estatística é opcional */ });
    },
    // novas mensagens privadas de outras pessoas (after=null só devolve o ponto de partida)
    inbox: async function (after) {
      var u = this.need(), self = this;
      if (after == null) {
        var l = await this.api('GET', '/rest/v1/messages?select=id&room=' + enc('like.dm:*') + '&order=id.desc&limit=1');
        return { last: l.length ? l[0].id : 0, items: [] };
      }
      var rows = await this.api('GET', '/rest/v1/messages?select=' + enc('*,profiles(name,avatar)') + '&room=' + enc('like.dm:*') + '&id=gt.' + enc(after) + '&order=id.asc&limit=50');
      var bl = await this.blocked(false), last = after;
      rows.forEach(function (r) { if (r.id > last) last = r.id; });
      return { last: last, items: rows.filter(function (r) { return r.uid !== u.id && bl.indexOf(r.uid) < 0 && r.room.split(':').slice(1, 3).indexOf(u.id) >= 0; }).map(function (r) { return self.msgOut(r); }) };
    },
    setBlock: async function (peer, on) {
      var u = this.need();
      if (on) await this.api('POST', '/rest/v1/blocks?on_conflict=blocker,blocked', { headers: { Prefer: 'resolution=merge-duplicates,return=minimal' }, body: { blocker: u.id, blocked: peer } });
      else await this.api('DELETE', '/rest/v1/blocks?blocker=eq.' + enc(u.id) + '&blocked=eq.' + enc(peer), { headers: { Prefer: 'return=minimal' } });
      this.blkCache = null;
    }
  };

  // =====================================================================
  // API pública (camada comum)
  // =====================================================================
  var P = demo, listeners = [], pend = null, timer = null;
  function emit(u) { listeners.slice().forEach(function (f) { try { f(u); } catch (e) { /* ignora */ } }); }
  function pick() {
    var c = W.POGGLOT_CONFIG;
    if (c && c.supabaseUrl && c.supabaseAnonKey) { sb.cfg = c; P = sb; } else P = demo;
    PogCloud.mode = P === sb ? 'supabase' : 'demo';
  }
  function needUser() { if (!P.user()) throw fail('Entre na sua conta para continuar.', 'auth'); }

  async function flush() {
    if (timer) { clearTimeout(timer); timer = null; }
    var s = pend; pend = null;
    if (!s || !P.user()) return;
    try { await P.pushStats(s); } catch (e) { if (!pend) pend = s; throw e; }
  }

  function subscribe(room, cb, opts) {
    checkRoom(room); opts = opts || {};
    var ms = Math.max(1000, opts.intervalMs || 3000), last = opts.after == null ? null : opts.after;
    var stopped = false, busy = false, t = null, doc = W.document;
    function schedule() { if (!stopped) t = setTimeout(tick, ms); }
    async function tick() {
      if (stopped) return;
      if (busy || (doc && doc.hidden) || !P.user()) return schedule();
      busy = true;
      try {
        if (last == null) { // 1ª rodada sem "after": só marca o ponto de partida
          var l = await PogCloud.messages(room, { limit: 1 });
          last = l.length ? l[l.length - 1].id : 0;
        } else {
          var n = await PogCloud.messages(room, { after: last, limit: 100 });
          if (n.length) { last = n[n.length - 1].id; try { cb(n); } catch (e) { /* erro do chamador */ } }
        }
      } catch (e) { if (opts.onError) try { opts.onError(e); } catch (e2) { /* ignora */ } }
      busy = false; schedule();
    }
    function onVis() { if (doc && !doc.hidden && !stopped && !busy) { clearTimeout(t); tick(); } }
    if (doc && doc.addEventListener) doc.addEventListener('visibilitychange', onVis);
    schedule();
    return function () {
      stopped = true; clearTimeout(t);
      if (doc && doc.removeEventListener) doc.removeEventListener('visibilitychange', onVis);
    };
  }

  var PogCloud = {
    mode: 'demo',
    rooms: ROOMS,
    init: async function () { pick(); await P.init(); return P.user(); },
    user: function () { return P.user(); },
    onAuth: function (fn) {
      listeners.push(fn);
      return function () { var i = listeners.indexOf(fn); if (i >= 0) listeners.splice(i, 1); };
    },
    signUp: async function (d) { var u = await P.signUp(d || {}); emit(u); return u; },
    signIn: async function (email, password) { var u = await P.signIn(email, password); emit(u); return u; },
    signOut: async function () {
      try { await flush(); } catch (e) { /* tenta salvar antes de sair */ }
      pend = null; await P.signOut(); emit(null);
    },
    resetPassword: function (email) { return P.resetPassword(email); },
    updateProfile: async function (p) { needUser(); return P.updateProfile(p); },
    pushStats: async function (s) {
      if (!P.user()) return;
      pend = checkStats(s);
      if (!P.statsDelay) return flush();
      if (!timer) timer = setTimeout(function () { timer = null; flush().catch(noop); }, P.statsDelay); // a última chamada vence
    },
    flush: flush,
    leaderboard: async function (o) {
      o = o || {};
      var by = ['xp', 'streak', 'eps'].indexOf(o.by) >= 0 ? o.by : 'xp';
      return P.leaderboard({ lang: o.lang || null, by: by, limit: Math.max(1, Math.min(o.limit || 50, 200)) });
    },
    members: async function (o) {
      o = o || {}; needUser();
      return P.searchMembers({ q: str(o.q, 60), native: o.native || null, learning: o.learning || null, limit: Math.max(1, Math.min(o.limit || 50, 200)) });
    },
    getProfile: async function (id) { needUser(); return P.getProfile(String(id)); },
    messages: async function (room, o) {
      o = o || {}; checkRoom(room); needUser();
      return P.messages(room, { after: o.after == null ? null : o.after, limit: Math.max(1, Math.min(o.limit || 60, 200)) });
    },
    send: async function (room, text, o) {
      checkRoom(room); needUser(); text = checkText(text);
      return P.send(room, text, o && o.fixOf != null ? o.fixOf : null, o && o.audio ? String(o.audio) : null);
    },
    voiceSupported: function () { return P === sb && !!(W.navigator && W.navigator.mediaDevices && W.MediaRecorder); },
    uploadVoice: function (blob) { needUser(); if (P !== sb) throw fail('Mensagens de voz precisam do servidor configurado.', 'demo'); return sb.uploadVoice(blob); },
    voiceUrl: function (path) { needUser(); return sb.voiceUrl(String(path)); },
    weekly: async function (o) {
      o = o || {}; needUser();
      if (P === sb) return sb.weekly({ limit: Math.max(1, Math.min(o.limit || 200, 200)) });
      return demo.allProfiles().map(function (p) { var q = pubProfile(p); q.week = Math.round((p.xp || 0) % 480); return q; }).sort(function (a, b) { return b.week - a.week; });
    },
    profileStats: async function (id) {
      needUser();
      if (P === sb) return sb.profileStats(String(id));
      return { questions: 0, answers: 0, likes: 0, best: 0, invited: 0 };
    },
    logEpisode: function (kind, cid, n, score) { try { if (P === sb) sb.logEpisode(kind, cid, n, score); } catch (e) { /* ignora */ } },
    inviteLink: function () { var u = P.user(); if (!u || P !== sb) return ''; return W.location.origin + W.location.pathname + '?ref=' + u.id; },
    // acesso REST autenticado (usado pelo fórum); só no modo Supabase
    rest: function (method, path, o) { needUser(); if (P !== sb) throw fail('Disponível só com o servidor configurado.', 'demo'); return sb.api(method, path, o); },
    subscribe: subscribe,
    // avisa de novas mensagens privadas (aba aberta, também em segundo plano; 20 s visível / 60 s oculta)
    watchInbox: function (cb) {
      var stopped = false, t = null, busy = false, doc = W.document, key = 'pogglot:inbox:', last = null;
      function uid() { var u = P.user(); return u && u.id; }
      function load() { try { var v = W.localStorage.getItem(key + uid()); return v == null ? null : Number(v); } catch (e) { return null; } }
      function save(v) { try { W.localStorage.setItem(key + uid(), String(v)); } catch (e) { /* ignora */ } }
      function next() { if (!stopped) t = setTimeout(tick, doc && doc.hidden ? 60000 : 20000); }
      async function tick() {
        if (stopped) return;
        if (busy || !P.user() || typeof P.inbox !== 'function') return next();
        busy = true;
        try {
          if (last == null) last = load();
          var r = await P.inbox(last);
          if (last == null || r.last > last) { last = r.last; save(last); }
          if (r.items.length) { try { cb(r.items); } catch (e) { /* erro do chamador */ } }
        } catch (e) { /* tenta de novo no próximo ciclo */ }
        busy = false; next();
      }
      t = setTimeout(tick, 1500);
      return function () { stopped = true; clearTimeout(t); };
    },
    dmRoom: function (peerId) { var u = P.user(); if (!u) throw fail('Entre na sua conta para continuar.', 'auth'); return 'dm:' + [u.id, String(peerId)].sort().join(':'); },
    dmList: async function () { needUser(); return P.dmList(); },
    report: async function (msgId, reason) { needUser(); return P.report(msgId, str(reason, 300) || 'sem motivo'); },
    block: async function (peerId) { needUser(); return P.setBlock(String(peerId), true); },
    unblock: async function (peerId) { needUser(); return P.setBlock(String(peerId), false); }
  };

  pick();
  // envia números pendentes ao fechar/ocultar a página
  if (W.addEventListener) W.addEventListener('pagehide', function () { if (pend) flush().catch(noop); });
  W.PogCloud = PogCloud;
})(typeof window !== 'undefined' ? window : this);
