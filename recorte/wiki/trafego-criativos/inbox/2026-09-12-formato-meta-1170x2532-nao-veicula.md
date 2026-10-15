# 2026-09-12 — Peça em 1170×2532 não veicula na Meta

Fonte: lote `gram01-l9-var-avatar-2026-09-11` (peças 28–32 do CRIATIVOS-PRONTOS).

- O molde L9 foi construído sobre screenshot de iPhone (1170×2532 ≈ 1:2,16). Não é 9:16 (seria 1170×2080). O Ads
  Manager marca "não veiculável" em todos os posicionamentos.
- 9:16 (1080×1920) serve Reels/Stories. Feed, Explorar e feed do perfil pedem 1,91:1 a 4:5 — vídeo 9:16 lá pede corte.
- Correção sem regerar nada: `reformatar-meta.sh` corta folga do head (40 topo / 110 colo) e o teclado do painel
  (302 px) pro 9:16; pro 4:5 fica só rosto + faixa. VO copiada, custo zero.
- Regra pra próximos moldes: nascer em 1080×1920 e prever uma variante 4:5 (rosto + faixa) desde o desenho.
