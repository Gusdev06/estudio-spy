// Ferramentas do orquestrador (rodam no processo do servidor, fora do terminal do agente).
// Saldo em vídeos: o cliente aprova N vídeos num botão (a reserva acontece no clique, não no texto do agente),
// cada peça entregue consome 1, e o que sobrar volta ao saldo no fim do pedido.
// Geração paga só por gerar_midia: estima o preço com os arquivos reais e confere o teto antes de cada chamada.
import { createSdkMcpServer, tool } from '@anthropic-ai/claude-agent-sdk';
import { SPEC, NOMES } from './ferramentas-spec.mjs';
import { execFile } from 'node:child_process'; import { promisify } from 'node:util';
import fs from 'node:fs'; import path from 'node:path'; import crypto from 'node:crypto';

const sh = promisify(execFile);
export const PREVIA_USD = Number(process.env.PREVIA_USD || 1);                 // rostos/sondas antes da aprovação
export const TETO_MIDIA_POR_VIDEO_USD = Number(process.env.TETO_MIDIA_POR_VIDEO_USD || 6);
export { NOMES };

const texto = (o) => ({ content: [{ type: 'text', text: typeof o === 'string' ? o : JSON.stringify(o, null, 1) }] });
const erro = (t) => ({ content: [{ type: 'text', text: t }], isError: true });
// O cliente só enxerga saldo em vídeos: frase que fala de dinheiro sai inteira do que ele vê.
const DINHEIRO = /US\$|R\$|\$\s?\d|\bUSD\b|\bBRL\b|\bd[óo]lar(?:es)?\b|\breais\b|\bcentavos?\b|\bcust(?:o|os|ou|a|ar)\b|\bgast(?:o|os|ei|ou)\b|\bor[çc]amento\b/i;
export const semDinheiro = (t) => String(t || '').split('\n').map((l) => DINHEIRO.test(l) ? l.split(/(?<=[.!?…])\s+/).filter((f) => !DINHEIRO.test(f)).join(' ') : l).join('\n').replace(/\n{3,}/g, '\n\n').trim();
export const tetoMidia = (j) => PREVIA_USD + TETO_MIDIA_POR_VIDEO_USD * (j.reserva || 0);

// caminho relativo a job/ → absoluto, recusando qualquer coisa fora de job/ (inclusive symlink)
function dentroDoJob(j, rel) {
  const raiz = fs.realpathSync(path.join(j.cwd, 'job'));
  const abs = path.resolve(raiz, String(rel).replace(/^\/w\//, '').replace(/^job\//, ''));   // no container o agente vê /w/job/…
  const real = fs.existsSync(abs) ? fs.realpathSync(abs) : path.join(fs.realpathSync(path.dirname(abs)), path.basename(abs));
  if (!real.startsWith(raiz + path.sep)) throw new Error(`fora do job: ${rel}`);
  return real;
}
async function decodificaInteiro(arq) {
  if (!/\.(mp4|mov|webm|m4v|mp3|wav|m4a)$/i.test(arq)) return fs.statSync(arq).size > 0;
  try { const { stderr } = await sh('ffmpeg', ['-v', 'error', '-i', arq, '-f', 'null', '-'], { maxBuffer: 1e7 }); return !stderr.trim(); } catch { return false; }
}
async function baixar(url, destino) {
  for (let t = 0; t < 3; t++) {
    try { await sh('curl', ['-sSL', '--fail', '-o', destino, url], { timeout: 300e3 }); if (await decodificaInteiro(destino)) return true; } catch {}
  }
  return false;
}

export function executores(j, ctx) {
  // ctx: { evento, meta, log, saldo(email), ehAdmin(email) }
  // "@caminho" (solto, em lista ou em objeto) vira URL pública: o arquivo sobe antes (mesmo arquivo = mesmo upload por 24 h)
  const uploads = new Map();
  async function subir(rel) {
    const abs = dentroDoJob(j, rel);
    if (!uploads.has(abs)) uploads.set(abs, sh('wavespeed', ['upload', abs, '--json'], { timeout: 300e3, maxBuffer: 1e6 }).then(({ stdout }) => JSON.parse(stdout).url));
    return uploads.get(abs);
  }
  async function resolver(v) {
    if (typeof v === 'string') return v.startsWith('@') ? subir(v.slice(1)) : v;
    if (Array.isArray(v)) return Promise.all(v.map(resolver));
    if (v && typeof v === 'object') return Object.fromEntries(await Promise.all(Object.entries(v).map(async ([k, x]) => [k, await resolver(x)])));
    return v;
  }
  const inputsParaArgs = async (inputs) => {
    const args = [];
    for (const [k, v] of Object.entries(inputs || {})) { const r = await resolver(v); args.push('-i', `${k}=${typeof r === 'string' ? r : JSON.stringify(r)}`); }
    return args;
  };

  const cwdTrab = path.join(j.cwd, 'job', 'trabalho');
  async function cotar({ modelo, inputs, saida }) {
    let args; try { args = await inputsParaArgs(inputs); } catch (e) { return { erro: `Arquivo de entrada inválido: ${String(e.message).slice(0, 200)}` }; }
    try {
      const { stdout } = await sh('wavespeed', ['price', modelo, ...args, '--json'], { cwd: cwdTrab, timeout: 180e3, maxBuffer: 1e7 });
      const p = JSON.parse(stdout); const preco = Number(p.discounted_price ?? p.price);
      if (preco > 0) return { args, preco };
    } catch (e) { ctx.log({ job: j.id, aviso: 'preco', modelo, msg: String(e).slice(0, 300) }); }
    return { erro: `Não consegui estimar o preço de ${modelo} com esses inputs. Confira os parâmetros com a ferramenta ver_modelo.` };
  }
  function checarTeto(preco, oque) {
    const teto = tetoMidia(j), gasto = j.gastoMidia || 0;
    if (ctx.ehAdmin(j.dono) || gasto + preco <= teto) return null;
    ctx.log({ job: j.id, teto: 'estourou', oque, preco, gasto, limite: teto });
    return j.reserva ? 'Limite de geração deste pedido atingido. Não gere mais nada: entregue o que já está pronto e explique ao cliente que o pedido chegou ao limite.'
                     : 'Isso precisa da aprovação do cliente antes. Mostre o plano/prévia e chame pedir_aprovacao.';
  }
  async function gerar({ modelo, saida }, { args, preco }) {
    const dir = path.join(cwdTrab, 'gerado'); fs.mkdirSync(dir, { recursive: true });
    const nome = saida.replace(/\//g, '-');
    let out;
    try {
      const { stdout } = await sh('wavespeed', ['run', modelo, ...args, '--json', '--download', path.join(dir, `${nome}-{index}.{ext}`)], { cwd: cwdTrab, timeout: 1200e3, maxBuffer: 2e7 });
      out = JSON.parse(stdout);
    } catch (e) {
      const m = /"id"\s*:\s*"([0-9a-f]{32})"/.exec(String(e.stdout || '') + String(e.stderr || ''));
      j.gastoMidia = (j.gastoMidia || 0) + preco; ctx.meta(j);
      ctx.log({ job: j.id, erro: 'run', modelo, id: m?.[1], msg: String(e).slice(0, 400) });
      return { erro: m ? `Erro de rede, mas a geração pode ter sido concluída (id ${m[1]}). Use recuperar_midia com esse id; NÃO gere de novo.`
                       : `A geração falhou: ${String(e.stderr || e.message).slice(0, 300)}` };
    }
    j.gastoMidia = (j.gastoMidia || 0) + preco; (j.predicoes ||= []).push({ id: out.id, modelo, preco, t: new Date().toISOString() }); ctx.meta(j);
    const arquivos = [];
    for (const [i, url] of (out.outputs || []).entries()) {
      let arq = out.saved?.[i];
      if (!arq || !(await decodificaInteiro(arq))) { arq = arq || path.join(dir, `${nome}-${i}${path.extname(new URL(url).pathname)}`); if (!(await baixar(url, arq))) { arquivos.push({ url, erro: 'download falhou' }); continue; } }
      arquivos.push(path.relative(j.cwd, arq));
    }
    return { id: out.id, arquivos };
  }

  return {
    pedir_aprovacao: async ({ videos, resumo }) => {
        const pend = j.eventos.find((e) => e.tipo === 'aprovacao' && e.estado === 'pendente');
        if (pend) pend.estado = 'substituida';
        const id = crypto.randomBytes(4).toString('hex');
        ctx.evento(j, { tipo: 'aprovacao', id, videos, resumo: semDinheiro(resumo) || `Vou fazer ${videos} vídeo(s).`, estado: 'pendente' });
        return texto(`Botão de aprovação de ${videos} vídeo(s) mostrado ao cliente. Termine a sua vez agora e espere a resposta. Saldo atual dele: ${ctx.ehAdmin(j.dono) ? 'ilimitado (admin)' : ctx.saldo(j.dono) + ' vídeo(s)'}.`);
      },

    gerar_midia: async (item) => {
        const c = await cotar(item); if (c.erro) return erro(c.erro);
        const t = checarTeto(c.preco, item.modelo); if (t) return erro(t);
        const r = await gerar(item, c); return r.erro ? erro(r.erro) : texto({ ...r, aviso: 'Confira o arquivo inteiro antes de usar.' });
      },

    gerar_midia_lote: async ({ itens }) => {
        // cota tudo em paralelo, confere o teto pelo TOTAL e só então dispara todas as gerações juntas
        const cot = await Promise.all(itens.map(cotar));
        const falhas = cot.map((c, i) => c.erro && `${itens[i].saida}: ${c.erro}`).filter(Boolean);
        if (falhas.length) return erro(`Nada foi gerado. Corrija e mande o lote de novo:\n${falhas.join('\n')}`);
        const total = cot.reduce((s, c) => s + c.preco, 0);
        const t = checarTeto(total, `lote de ${itens.length}`); if (t) return erro(t);
        const res = await Promise.all(itens.map((it, i) => gerar(it, cot[i]).then((r) => ({ saida: it.saida, ...r }))));
        return texto({ resultados: res, aviso: 'Confira cada arquivo inteiro antes de usar. Para os que deram erro com id, use recuperar_midia (não gere de novo).' });
      },

    recuperar_midia: async ({ id, saida }) => {
        try {
          const { stdout } = await sh('wavespeed', ['show', id, '--json'], { timeout: 60e3, maxBuffer: 1e7 });
          const p = JSON.parse(stdout); const outs = p.outputs || p.raw?.outputs || [];
          if (!outs.length) return erro(`Sem resultado ainda (status: ${p.status || '?'}). Tente de novo em 1 minuto.`);
          const dir = path.join(j.cwd, 'job', 'trabalho', 'gerado'); fs.mkdirSync(dir, { recursive: true });
          const salvos = [];
          for (const [i, url] of outs.entries()) { const arq = path.join(dir, `${saida.replace(/\//g, '-')}-${i}${path.extname(new URL(url).pathname)}`);
            salvos.push((await baixar(url, arq)) ? path.relative(j.cwd, arq) : { url, erro: 'download falhou' }); }
          return texto({ id, arquivos: salvos });
        } catch (e) { return erro(`Não consegui recuperar: ${String(e.message).slice(0, 200)}`); }
      },

    entregar_video: async ({ caminho }) => {
        let arq; try { arq = dentroDoJob(j, caminho); } catch (e) { return erro(String(e.message)); }
        const rel = path.relative(j.cwd, arq);
        if (!/^job\/saida\/[^/]+\.(mp4|mov|webm|jpg|jpeg|png|webp)$/i.test(rel) || !fs.existsSync(arq)) return erro('A peça precisa estar em job/saida/ (vídeo ou imagem).');
        if ((j.entregues || []).includes(rel)) return texto(`Já estava entregue: ${rel}`);
        if (!ctx.ehAdmin(j.dono) && (j.entregues || []).length >= (j.reserva || 0)) return erro('Não há vídeo reservado pra esta peça. Peça aprovação de mais vídeos com pedir_aprovacao.');
        if (!(await decodificaInteiro(arq))) return erro('O arquivo não decodifica inteiro. Remonte antes de entregar.');
        (j.entregues ||= []).push(rel); ctx.meta(j);
        ctx.evento(j, { tipo: 'entregue', caminho: rel });
        return texto(`Entregue (${j.entregues.length} de ${j.reserva || 0} reservados).`);
      },

    finalizar_pedido: async () => texto(ctx.finalizar(j)),

    ver_modelo: async ({ modelo }) => {
      try { const { stdout } = await sh('wavespeed', ['schema', modelo, '--json'], { timeout: 60e3, maxBuffer: 1e7 }); return texto(stdout.slice(0, 12000)); }
      catch (e) { return erro(`Modelo não encontrado ou sem schema: ${String(e.stderr || e.message).slice(0, 200)}`); }
    },
  };
}

// Modo local (agente no mesmo processo): MCP em processo com os executores.
export function servidorDeFerramentas(j, ctx) {
  const ex = executores(j, ctx);
  return createSdkMcpServer({ name: 'estudio', version: '1.0.0',
    tools: Object.entries(SPEC).map(([nome, d]) => tool(nome, d.descricao, d.schema, (args) => ex[nome](args))) });
}

// Modo processo/container: o runner repassa a chamada por HTTP e o servidor executa aqui.
export async function executar(j, ctx, nome, args) {
  const ex = executores(j, ctx);
  if (!ex[nome]) return erro(`ferramenta desconhecida: ${nome}`);
  const parsed = (await import('zod')).z.object(SPEC[nome].schema).safeParse(args || {});
  if (!parsed.success) return erro(`argumentos inválidos: ${parsed.error.message.slice(0, 300)}`);
  return ex[nome](parsed.data);
}
