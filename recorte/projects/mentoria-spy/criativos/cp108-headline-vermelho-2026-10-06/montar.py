#!/usr/bin/env python3
# CP108 (podcast WPP, ruiva x negra afro, 49 s): 5 variações trocando SÓ a headline e o fundo preto -> vermelho (06/10/2026).
# Molde medido na 108: caixa da headline (246,246,246) x 17-703, y 139-271, raio ~22, Montserrat ExtraBold preta em 2 linhas;
# janela de vídeo 720x587 em y 346; karaokê em y 935 (PNGs RGBA do lote podcast-wpp-57s-copy-nova, idênticos aos da 108);
# a partir de 33,61 s o CTA ocupa o quadro inteiro (fica igual). Áudio copiado da 108 (bit-idêntico).
# Uso (de projects/mentoria-spy/): python3 criativos/cp108-headline-vermelho-2026-10-06/montar.py [v1 v2 ...]
import os, sys, subprocess
from PIL import Image, ImageDraw, ImageFont
L='criativos/cp108-headline-vermelho-2026-10-06'; REF=f'{L}/REFERENCIA-108.mp4'
KAR='centerpag-detect/criativos/podcast-wpp-57s-copy-nova-2026-09-23/karaoke/frames/%04d.png'
FONTE='gram-detect/criativos/var1-beatriz-aguiar-1622854622757052-2026-09-25/fontes/Montserrat.ttf'
VERMELHO='0xC8101E'; CTA=33.61; W,H=720,1280
HL={'v1':("HOW TO SEE WHO YOUR","PARTNER IS REALLY TEXTING"),
    'v2':("HOW TO RECOVER YOUR PARTNER'S","DELETED MESSAGES"),
    'v3':("READ YOUR PARTNER'S WHATSAPP","WITHOUT TOUCHING THEIR PHONE"),
    'v4':("SEE WHAT YOUR PARTNER DELETES","BEFORE YOU WAKE UP"),
    'v5':("THE TRUTH IS IN THE CHATS","YOUR PARTNER DELETED")}
def titulo(k):
    im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im)
    d.rounded_rectangle((17,139,703,271),radius=22,fill=(246,246,246,255))
    for s in range(34,20,-1):          # corpo da 108 (capital ~24 px = 34); só encolhe se passar de 650 px
        F=ImageFont.truetype(FONTE,s); F.set_variation_by_name('ExtraBold')
        if max(F.getlength(t) for t in HL[k])<=650: break
    for t,yc in zip(HL[k],(182,227)):
        d.text((W/2,yc),t,font=F,fill=(12,12,12,255),anchor='mm')
    p=f'{L}/titulos/{k}.png'; im.save(p); return p
for k in (sys.argv[1:] or list(HL)):
    t=titulo(k); out=f'{L}/pecas/108-headline-{k}-vermelho.mp4'
    fc=(f"color=c={VERMELHO}:s={W}x{H}:r=30:d=49[base];"
        f"[1:v]format=rgba,loop=loop=-1:size=1,fps=30[tit];[base][tit]overlay=0:0:enable='lt(t,{CTA})'[v1];"
        f"[0:v]crop=720:587:0:346[jan];[v1][jan]overlay=0:346:enable='lt(t,{CTA})'[v2];"
        f"[2:v]format=rgba[kar];[v2][kar]overlay=0:935:eof_action=pass:enable='lt(t,{CTA})'[v3];"
        f"[v3][0:v]overlay=0:0:enable='gte(t,{CTA})'[v]")
    cmd=['ffmpeg','-hide_banner','-v','error','-y','-i',REF,'-i',t,'-framerate','30','-start_number','0','-i',KAR,'-filter_complex',fc,
         '-map','[v]','-map','0:a','-c:a','copy','-frames:v','1470','-c:v','libx264','-preset','slow','-crf','18','-pix_fmt','yuv420p',
         '-colorspace','bt709','-color_primaries','bt709','-color_trc','bt709','-color_range','tv','-movflags','+faststart',out]
    subprocess.run(cmd,check=True); print('ok ->',out)
