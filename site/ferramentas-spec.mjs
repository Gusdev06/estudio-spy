// Definição das ferramentas do Estúdio (nome, descrição, schema). Compartilhada entre o servidor (que executa)
// e o runner do container (que só repassa a chamada ao servidor). Nenhuma lógica nem segredo aqui.
import { z } from 'zod';

export const SPEC = {
  pedir_aprovacao: {
    descricao: 'Mostra ao cliente um botão "Aprovar" que reserva N vídeos do saldo dele. Chame quando já souber o que variar, o avatar e quantas variações, ANTES de qualquer geração paga de vídeo. Depois de chamar, termine a sua vez e espere: a aprovação chega como mensagem do cliente.',
    schema: { videos: z.number().int().min(1).max(20).describe('quantas peças finais serão entregues (1 peça = 1 vídeo do saldo)'),
              resumo: z.string().max(400).describe('UMA linha pro cliente: o que será entregue e em quanto tempo fica pronto') },
  },
  gerar_midia: {
    descricao: 'ÚNICA forma de gerar mídia paga (imagem, vídeo, lipsync, voz, transcrição). Equivale a `wavespeed run <modelo> -i chave=valor`. Arquivos locais: valor "@caminho" relativo a job/ (ex.: "@trabalho/rosto/a1.png"). Estima o preço com os arquivos reais e recusa se passar do limite do pedido. Antes da aprovação só cabe prévia barata (rosto, sonda). Pra várias gerações independentes, use gerar_midia_lote.',
    schema: { modelo: z.string().max(120).describe('id do modelo, ex.: openai/gpt-image-2/edit'),
              inputs: z.record(z.string(), z.any()).describe('inputs do modelo; arquivos como "@trabalho/…"'),
              saida: z.string().max(120).regex(/^[\w\-\/]+$/).describe('nome base dentro de job/trabalho/gerado/, sem extensão, ex.: rosto-v1') },
  },
  gerar_midia_lote: {
    descricao: 'Gera VÁRIAS mídias pagas AO MESMO TEMPO (mesmo formato de gerar_midia, uma por item). Use sempre que houver mais de uma geração independente (ex.: os rostos das 3 variações, os lipsyncs das 3 variações): é muito mais rápido que uma por vez. O limite do pedido é conferido pelo total antes de gerar.',
    schema: { itens: z.array(z.object({
      modelo: z.string().max(120), inputs: z.record(z.string(), z.any()), saida: z.string().max(120).regex(/^[\w\-\/]+$/),
    })).min(1).max(12) },
  },
  ver_modelo: {
    descricao: 'Mostra os parâmetros (schema) de um modelo de geração, sem gerar nada nem gastar. Equivale a `wavespeed schema <modelo>`.',
    schema: { modelo: z.string().max(120) },
  },
  recuperar_midia: {
    descricao: 'Baixa o resultado de uma geração que já foi feita (pelo id), sem gerar de novo nem pagar outra vez.',
    schema: { id: z.string().regex(/^[0-9a-f]{32}$/), saida: z.string().max(120).regex(/^[\w\-\/]+$/) },
  },
  entregar_video: {
    descricao: 'Registra uma peça final como entregue ao cliente (consome 1 vídeo da reserva). Só pra peças finais em job/saida/, já conferidas.',
    schema: { caminho: z.string().max(200).describe('ex.: job/saida/variacao-1.mp4') },
  },
  finalizar_pedido: {
    descricao: 'Chame quando tudo o que foi pedido estiver entregue: devolve ao saldo do cliente os vídeos reservados e não usados.',
    schema: {},
  },
};
export const NOMES = Object.keys(SPEC).map((n) => `mcp__estudio__${n}`);
