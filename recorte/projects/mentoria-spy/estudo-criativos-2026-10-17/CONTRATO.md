# Contrato do estudo (17/10/2026)

Cada analista recebe uma lista (`lista-*.json`, caminhos relativos a `projects/mentoria-spy/`) e devolve **um** arquivo `estudo-<nome>.json` nesta pasta, com uma entrada por criativo:

```json
{
  "id": "<id da Ad Library>",
  "arquivo": "<caminho como veio na lista>",
  "pagina": "...", "ref": "<PPA25… ou ->", "funil": "<path do link ou host>", "dias": 0,
  "formato": "video|imagem", "duracao_s": 0,
  "idioma": "en|es|fr|pt",
  "headline": "<texto principal na tela nos 3 primeiros segundos, literal>",
  "primeira_fala": "<primeira frase falada, literal; '-' se mudo>",
  "transcricao": "<fala completa, literal; '-' se mudo>",
  "angulo": "<1 frase: qual dor/desejo explora>",
  "formato_criativo": "<ex.: talking head UGC, POV esquete + demo, podcast, estático app-mockup, notícia, split-screen>",
  "layout_catalogo": "<L1–L10 de wiki/trafego-criativos/wiki/tecnicas/catalogo-de-layouts-spy.md, ou 'novo: …'>",
  "estrutura": ["0-3s: …", "3-10s: …", "…"],
  "cta": "<literal>",
  "prova": "<o que usam como prova: demo do app, print, número…>",
  "producao": "<como foi feito: IA (qual sinal), gravado, stock, edição só de texto…>",
  "familia": "<rótulo curto pra agrupar criativos iguais/quase iguais, ex.: 'instaspy-everything-dark'>",
  "nota_analista": "<0-10: quão forte o gancho parece e por quê, 1 linha>",
  "variavel_barata": "<a variação mais barata que daria pra fazer (só edição) e qual alavanca mexe>"
}
```

Regras:
- **Literal.** Copie texto e fala como aparecem, sem traduzir e sem melhorar. Se não der pra ler, escreva `?`.
- Vídeo: transcreva com `python3 ~/.claude/skills/watch/scripts/whisper.py <arquivo>` (Groq; o Whisper inventa "Thank you." em trecho mudo, então ignore fala com menos de 6 palavras distintas). Veja os frames com ffmpeg (folha de contato de 1 fps) e **abra a imagem**.
- Imagem: abra e leia.
- Agrupe criativos quase iguais na mesma `familia`.
- `dias` = dias no ar (está no manifest: campo `dias`, ou calcule a partir de `inicio` com hoje = 17/10/2026).
- Não gaste em geração paga. Não escreva fora do seu arquivo `estudo-<nome>.json` (e de uma pasta `tmp-<nome>/` sua para frames).
- No fim, um `estudo-<nome>.md` curto: as 5 famílias mais fortes e por quê, com os ids.
