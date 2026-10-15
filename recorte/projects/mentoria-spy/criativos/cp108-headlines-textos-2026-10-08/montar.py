#!/usr/bin/env python3
# CP108 (podcast WPP, ruiva x negra afro, 49 s): 5 headlines novas, fundo PRETO original (08/10/2026) -> peças 189-193.
# Molde medido na 108 (CRIATIVOS-PRONTOS): faixa de cima (y 0-345) é estática até o frame 1008 (diferença <= 11 níveis,
# só compressão): preto + caixa (244,244,244 decodificado) x 17-703, y 139-271, raio ~22; texto Montserrat ExtraBold,
# corpo 35 (larguras medidas 610/638 px batem com 613/641 do original), 2 linhas centradas em y 182 e 227.
# A faixa inteira é REDESENHADA (preto + caixa + texto novo, opaca) e cobre y 0-345 nos frames 0-1008; o CTA começa no
# frame 1009 (33,633 s) e fica igual. Janela (y 346) e karaokê (y 935) são os da própria 108; áudio copiado (bit-idêntico).
# Uso (de projects/mentoria-spy/): python3 criativos/cp108-headlines-textos-2026-10-08/montar.py [189 190 ...]
import sys, subprocess
from PIL import Image, ImageDraw, ImageFont
L='criativos/cp108-headlines-textos-2026-10-08'
MAE='CRIATIVOS-PRONTOS/108-ZAP-podcast-wpp-copy-nova-branca-ruiva-x-negra-afro.mp4'
FONTE='gram-detect/criativos/var1-beatriz-aguiar-1622854622757052-2026-09-25/fontes/Montserrat.ttf'
W,FAIXA,ULT=720,346,1008   # último frame com título
PECAS={'189':('chats-que-ele-nao-queria-mostrar',("THE CHATS YOUR PARTNER","NEVER WANTED YOU TO SEE")),
       '190':('digitei-o-numero-vi-tudo',("I TYPED HIS NUMBER","AND SAW EVERY CHAT")),
       '191':('o-que-ele-manda-as-2h',("WHAT DOES YOUR PARTNER SEND","AT 2 IN THE MORNING?")),
       '192':('chats-em-60-segundos',("ALL YOUR PARTNER'S CHATS","ON YOUR PHONE IN 60 SECONDS")),
       '193':('apagadas-ainda-estao-la',("YOUR PARTNER'S DELETED CHATS","ARE STILL THERE TO READ"))}
CAIXA=int(sys.argv[sys.argv.index('--caixa')+1]) if '--caixa' in sys.argv else 246
def faixa(n):
    linhas=PECAS[n][1]; im=Image.new('RGB',(W,FAIXA),(0,0,0)); d=ImageDraw.Draw(im)
    d.rounded_rectangle((17,139,703,271),radius=22,fill=(CAIXA,)*3)
    for s in (35,34,33,32,31,30,29,28):      # corpo da 108; só encolhe se uma linha passar de 650 px
        F=ImageFont.truetype(FONTE,s); F.set_variation_by_name('ExtraBold')
        if max(F.getlength(t) for t in linhas)<=650: break
    for t,yc in zip(linhas,(182,227)): d.text((W/2,yc),t,font=F,fill=(12,12,12),anchor='mm')
    p=f'{L}/titulos/{n}.png'; im.save(p); return p,s
for n in [a for a in sys.argv[1:] if a in PECAS] or list(PECAS):
    t,s=faixa(n); out=f'{L}/pecas/{n}-ZAP-podcast-wpp-{PECAS[n][0]}.mp4'
    fc=f"[1:v]format=rgb24,loop=loop=-1:size=1,fps=30[t];[0:v][t]overlay=0:0:shortest=0:eof_action=pass:enable='lte(n,{ULT})'[v]"
    cmd=['ffmpeg','-hide_banner','-v','error','-y','-i',MAE,'-i',t,'-filter_complex',fc,'-map','[v]','-map','0:a','-c:a','copy',
         '-frames:v','1470','-c:v','libx264','-preset','slow','-crf','18','-pix_fmt','yuv420p','-colorspace','bt709',
         '-color_primaries','bt709','-color_trc','bt709','-color_range','tv','-map_metadata','-1','-movflags','+faststart',out]
    subprocess.run(cmd,check=True); print('ok ->',out,'corpo',s)
