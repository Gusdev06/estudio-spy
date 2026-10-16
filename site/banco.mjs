// Banco do Estúdio: schema `estudio` no Supabase (o mesmo projeto do HookMill, com usuário próprio que só enxerga este schema).
// O servidor trabalha em memória e grava aqui em segundo plano, numa fila em ordem com nova tentativa. O disco (_usuarios.json etc.)
// continua sendo escrito como cópia de segurança: se o banco cair no boot, o servidor sobe pelo disco.
import pg from 'pg';

const TABELAS = `
create table if not exists estudio.usuarios (email text primary key, videos int not null default 0, dados jsonb not null, atualizado timestamptz not null default now());
create table if not exists estudio.sessoes (hash text primary key, email text not null, ate timestamptz not null);
create table if not exists estudio.pagamentos (id text primary key, dados jsonb not null, atualizado timestamptz not null default now());
create table if not exists estudio.pendentes (email text primary key, videos int not null);
create table if not exists estudio.pedidos (id text primary key, dono text not null, dados jsonb not null, criado timestamptz not null default now(), atualizado timestamptz not null default now());
create index if not exists pedidos_dono on estudio.pedidos (dono);
create table if not exists estudio.eventos (pedido text not null, n int not null, t timestamptz not null, tipo text not null, dados jsonb not null, primary key (pedido, n));
create table if not exists estudio.config (chave text primary key, valor jsonb);
create table if not exists estudio.convites (token text primary key, dados jsonb not null, atualizado timestamptz not null default now());`;

export async function abrirBanco(url, log) {
  if (!url) return null;
  const pool = new pg.Pool({ connectionString: url, ssl: /@(localhost|127\.0\.0\.1)[:/]/.test(url) ? false : { rejectUnauthorized: false }, max: Number(process.env.BANCO_CONEXOES || 4), idleTimeoutMillis: 30e3, connectionTimeoutMillis: 10e3 });
  pool.on('error', (e) => log({ erro: 'banco', msg: String(e.message || e) }));
  await pool.query(TABELAS);

  // fila única e em ordem: cada escrita tenta 4 vezes (1 s, 5 s, 15 s) antes de desistir e registrar no log
  let fila = Promise.resolve(), pendentes = 0, falhas = 0;
  const espera = (ms) => new Promise((r) => setTimeout(r, ms));
  const enfileirar = (nome, fn) => { pendentes++;
    fila = fila.then(async () => {
      for (const [i, ms] of [0, 1e3, 5e3, 15e3].entries()) {
        if (ms) await espera(ms);
        try { await fn(); return; } catch (e) { if (i === 3) { falhas++; log({ erro: 'banco-escrita', nome, msg: String(e.message || e).slice(0, 300) }); } }
      }
    }).finally(() => pendentes--); };

  // só grava o que mudou desde a última escrita (o servidor chama "salvar tudo" a cada alteração)
  const ultimo = { convites: new Map(), usuarios: new Map(), sessoes: new Map(), pagamentos: new Map(), pendentes: new Map(), pedidos: new Map() };
  const mudou = (mapa, chave, valor) => { const s = JSON.stringify(valor); if (mapa.get(chave) === s) return false; mapa.set(chave, s); return true; };
  const sumiu = (mapa, atuais) => [...mapa.keys()].filter((k) => !atuais.has(k)).map((k) => (mapa.delete(k), k));

  return {
    get pendentes() { return pendentes; }, get falhas() { return falhas; },
    esvaziar: () => fila,

    async carregar() {
      const migrado = (await pool.query(`select valor from estudio.config where chave = 'migrado'`)).rows[0]?.valor;
      if (!migrado) return null;
      const convites = {}; for (const r of (await pool.query('select token, dados from estudio.convites')).rows) { convites[r.token] = r.dados; mudou(ultimo.convites, r.token, r.dados); }
      const usuarios = {}, sessoes = new Map(), pagamentos = { pedidos: {}, pendentes: {} }, pedidos = new Map();
      for (const r of (await pool.query('select email, videos, dados from estudio.usuarios')).rows) { usuarios[r.email] = { ...r.dados, videos: r.videos }; mudou(ultimo.usuarios, r.email, usuarios[r.email]); }
      for (const r of (await pool.query('select hash, email, ate from estudio.sessoes where ate > now()')).rows) { const s = { email: r.email, ate: r.ate.getTime() }; sessoes.set(r.hash, s); mudou(ultimo.sessoes, r.hash, s); }
      for (const r of (await pool.query('select id, dados from estudio.pagamentos')).rows) { pagamentos.pedidos[r.id] = r.dados; mudou(ultimo.pagamentos, r.id, r.dados); }
      for (const r of (await pool.query('select email, videos from estudio.pendentes')).rows) { pagamentos.pendentes[r.email] = r.videos; mudou(ultimo.pendentes, r.email, r.videos); }
      for (const r of (await pool.query('select id, dados from estudio.pedidos')).rows) { pedidos.set(r.id, { dados: r.dados, eventos: [] }); mudou(ultimo.pedidos, r.id, r.dados); }
      for (const r of (await pool.query('select pedido, dados from estudio.eventos order by pedido, n')).rows) pedidos.get(r.pedido)?.eventos.push(r.dados);
      return { usuarios, sessoes, pagamentos, pedidos, convites };
    },
    marcarMigrado: () => enfileirar('migrado', () => pool.query(`insert into estudio.config values ('migrado', $1) on conflict (chave) do update set valor = $1`, [JSON.stringify(new Date().toISOString())])),

    usuarios(todos) {
      const muda = Object.entries(todos).filter(([e, u]) => mudou(ultimo.usuarios, e, u));
      const fora = sumiu(ultimo.usuarios, new Set(Object.keys(todos)));
      if (!muda.length && !fora.length) return;
      enfileirar('usuarios', async () => {
        for (const [e, u] of muda) { const { videos = 0, ...dados } = u;
          await pool.query(`insert into estudio.usuarios (email, videos, dados) values ($1, $2, $3) on conflict (email) do update set videos = $2, dados = $3, atualizado = now()`, [e, videos, dados]); }
        if (fora.length) await pool.query('delete from estudio.usuarios where email = any($1)', [fora]);
      });
    },
    sessoes(mapa) {
      const muda = [...mapa].filter(([h, s]) => mudou(ultimo.sessoes, h, s));
      const fora = sumiu(ultimo.sessoes, new Set(mapa.keys()));
      if (!muda.length && !fora.length) return;
      enfileirar('sessoes', async () => {
        for (const [h, s] of muda) await pool.query(`insert into estudio.sessoes values ($1, $2, to_timestamp($3 / 1000.0)) on conflict (hash) do update set ate = excluded.ate`, [h, s.email, s.ate]);
        if (fora.length) await pool.query('delete from estudio.sessoes where hash = any($1) or ate < now()', [fora]);
      });
    },
    pagamentos(pg_) {
      const muda = Object.entries(pg_.pedidos).filter(([id, d]) => mudou(ultimo.pagamentos, id, d));
      const pend = Object.entries(pg_.pendentes).filter(([e, n]) => mudou(ultimo.pendentes, e, n));
      const pendFora = sumiu(ultimo.pendentes, new Set(Object.keys(pg_.pendentes)));
      if (!muda.length && !pend.length && !pendFora.length) return;
      enfileirar('pagamentos', async () => {
        for (const [id, d] of muda) await pool.query(`insert into estudio.pagamentos (id, dados) values ($1, $2) on conflict (id) do update set dados = $2, atualizado = now()`, [id, d]);
        for (const [e, n] of pend) await pool.query(`insert into estudio.pendentes values ($1, $2) on conflict (email) do update set videos = $2`, [e, n]);
        if (pendFora.length) await pool.query('delete from estudio.pendentes where email = any($1)', [pendFora]);
      });
    },
    convites(todos) {
      const muda = Object.entries(todos).filter(([t, c]) => mudou(ultimo.convites, t, c));
      if (!muda.length) return;
      enfileirar('convites', async () => { for (const [t, c] of muda) await pool.query(`insert into estudio.convites (token, dados) values ($1, $2) on conflict (token) do update set dados = $2, atualizado = now()`, [t, c]); });
    },
    pedido(id, dono, dados) {
      if (!mudou(ultimo.pedidos, id, dados)) return;
      enfileirar('pedido', () => pool.query(`insert into estudio.pedidos (id, dono, dados) values ($1, $2, $3) on conflict (id) do update set dono = $2, dados = $3, atualizado = now()`, [id, dono, dados]));
    },
    evento(id, e) {
      enfileirar('evento', () => pool.query(`insert into estudio.eventos values ($1, $2, to_timestamp($3 / 1000.0), $4, $5) on conflict (pedido, n) do update set dados = $5`, [id, e.n, e.t, e.tipo, e]));
    },
    apagarPedido(id) { ultimo.pedidos.delete(id);
      enfileirar('apagar', async () => { await pool.query('delete from estudio.eventos where pedido = $1', [id]); await pool.query('delete from estudio.pedidos where id = $1', [id]); }); },
    async fechar() { await fila; await pool.end(); },
  };
}
