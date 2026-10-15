#!/usr/bin/env python3
"""Copia anuncios/ -> tratados/ com os metadados zerados.

- .mp4  : remux sem re-encodar (-c copy -map_metadata -1). Some a tag `title` que a Meta
          carimba com o ID do vídeo. Pixel a pixel é o mesmo arquivo.
- .jpg  : re-salva em qualidade alta sem EXIF/ICC.

Uso: python3 scripts/tratar-criativos.py
"""
import os, subprocess, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC, DST = os.path.join(RAIZ,'anuncios'), os.path.join(RAIZ,'tratados')
os.makedirs(DST, exist_ok=True)

for nome in sorted(os.listdir(SRC)):
    ent, sai = os.path.join(SRC,nome), os.path.join(DST,nome)
    if nome.endswith('.mp4'):
        cmd = ['ffmpeg','-y','-loglevel','error','-i',ent,'-c','copy',
               '-map_metadata','-1','-movflags','+faststart',sai]
    elif nome.endswith(('.jpg','.jpeg','.png')):
        cmd = ['ffmpeg','-y','-loglevel','error','-i',ent,'-map_metadata','-1',
               '-q:v','2',sai]
    else:
        continue
    subprocess.run(cmd, check=True)
    print(nome, flush=True)
print('ok')
