#!/usr/bin/env node
// Runner do agente: roda DENTRO do container de um pedido (ou como subprocesso no modo "processo").
// Lê a especificação da rodada no stdin (JSON), executa o Claude Agent SDK com cwd = pasta de trabalho
// e escreve cada mensagem do SDK como uma linha JSON no stdout. Não tem chave nenhuma:
//  - o modelo é chamado por ANTHROPIC_BASE_URL (proxy do servidor) com um token temporário do pedido;
//  - as ferramentas do Estúdio (geração paga, aprovação, entrega) só repassam a chamada ao servidor (ORQ_URL + ORQ_TOKEN).
import { query, createSdkMcpServer, tool } from '@anthropic-ai/claude-agent-sdk';
import { SPEC, NOMES } from './ferramentas-spec.mjs';
import { trava } from './trava.mjs';

const ORQ_URL = process.env.ORQ_URL, ORQ_TOKEN = process.env.ORQ_TOKEN, JOB_ID = process.env.JOB_ID;
const sai = (o) => process.stdout.write(JSON.stringify(o) + '\n');
if (!ORQ_URL || !ORQ_TOKEN) { sai({ type: 'runner_erro', erro: 'ORQ_URL/ORQ_TOKEN ausentes' }); process.exit(2); }

let entrada = ''; for await (const c of process.stdin) entrada += c;
const spec = JSON.parse(entrada);   // { prompt, resume, model, maxTurns, sistema, allowedTools }

const repassa = (nome) => async (args) => {
  try {
    const r = await fetch(`${ORQ_URL}/interno/${ORQ_TOKEN}/ferramenta/${nome}`, {
      method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify(args ?? {}), signal: AbortSignal.timeout(1500e3) });
    if (!r.ok) return { content: [{ type: 'text', text: `Ferramenta indisponível agora (${r.status}). Tente de novo em instantes.` }], isError: true };
    return await r.json();
  } catch (e) { return { content: [{ type: 'text', text: `Ferramenta indisponível agora: ${String(e.message).slice(0, 120)}` }], isError: true }; }
};
const estudio = createSdkMcpServer({ name: 'estudio', version: '1.0.0',
  tools: Object.entries(SPEC).map(([nome, d]) => tool(nome, d.descricao, d.schema, repassa(nome))) });

const log = (o) => sai({ type: 'runner_log', ...o });
try {
  const q = query({ prompt: spec.prompt, options: {
    cwd: process.cwd(), model: spec.model || 'claude-opus-5-5',
    systemPrompt: { type: 'preset', preset: 'claude_code', append: spec.sistema || '' },
    settingSources: ['project'],
    allowedTools: [...(spec.allowedTools || ['Bash', 'Read', 'Write', 'Edit', 'Glob', 'Grep', 'Skill', 'TodoWrite', 'Task']), ...NOMES],
    mcpServers: { estudio },
    permissionMode: 'bypassPermissions', maxTurns: spec.maxTurns || 300,
    hooks: { PreToolUse: [{ hooks: [trava(process.cwd(), log, JOB_ID)] }] },
    env: { ...process.env, BASH_DEFAULT_TIMEOUT_MS: '300000', BASH_MAX_TIMEOUT_MS: '900000' },
    ...(spec.resume ? { resume: spec.resume } : {}),
  } });
  for await (const m of q) sai(m);
} catch (e) { sai({ type: 'runner_erro', erro: String(e?.stack || e).slice(0, 2000) }); process.exit(1); }
