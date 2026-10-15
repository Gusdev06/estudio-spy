// Trava do terminal do agente (hook PreToolUse). Obstáculo, não fronteira: no modo container a fronteira é o próprio container
// (só a pasta do pedido, recorte somente leitura, sem rede e sem chave). Compartilhada entre o servidor (modo local) e o runner.
import path from 'node:path';

// Obstáculo, não fronteira (ver pronto-pra-vender S1/S2): o container por job do passo 2 substitui isto.
const PROIBIDO = /(?:\benv\b|printenv|environ|\/proc\/|Library\/Preferences|\.config\/|keychain|security\s+find|Documents\/AIS-OS|\.claude\/projects|\.ssh|\.aws|_usuarios\.json|_recorte|_servidor\.log|_bloqueios\.log|wavespeed\s+(?:run|show|history|balance|billings|delete|upload|download|status|login|logout|config|top-up|open)|api\.wavespeed\.ai)/i;
export const trava = (cwd, log = () => {}, meuId = path.basename(cwd)) => async (entrada) => {
  const s = JSON.stringify(entrada.tool_input || {});
  const outroJob = [...s.matchAll(/\d{12}-[0-9a-f]{4,6}/g)].some(([id]) => id !== meuId);
  const sobeDemais = /(?:\.\.[\/\\]+){2,}\.\./.test(s);   // job/trabalho/../../.. já é a pasta de todos os jobs
  const foraDoJob = [...s.matchAll(/\/(?:Users|home|root|private|tmp|var|etc|opt)\/[^\s"'`;|&)]*/gi)].some(([c]) => !c.startsWith(cwd) && !/^\/(?:usr|bin|opt\/homebrew)\//.test(c));   // caminho absoluto só dentro do próprio job
  if (PROIBIDO.test(s) || outroJob || sobeDemais || foraDoJob) {
    log({ trava: meuId, ferramenta: entrada.tool_name, entrada: s.slice(0, 300) });
    return { hookSpecificOutput: { hookEventName: 'PreToolUse', permissionDecision: 'deny',
      permissionDecisionReason: 'Bloqueado: fora do job ou acesso a credencial. Trabalhe só dentro do workspace.' } };
  }
  return {};
};

