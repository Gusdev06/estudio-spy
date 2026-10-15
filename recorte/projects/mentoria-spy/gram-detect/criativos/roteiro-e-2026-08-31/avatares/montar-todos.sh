#!/bin/bash
set -e; cd "$(dirname "$0")/.."
for av in a1-homem-velho a2-mulher-velha a3-jovem; do
  D=avatares/$av
  printf "file '%s'\n" 01.mp4 02.mp4 03.mp4 04.mp4 05.mp4 > $D/lista.txt
  (cd $D && ffmpeg -v error -f concat -safe 0 -i lista.txt -c copy ../../avatares/$av-bruto.mp4 -y)
  IN=avatares/$av-bruto.mp4
  DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$IN")
  ffmpeg -i "$IN" -af silencedetect=noise=-34dB:d=0.45 -f null /dev/null 2>&1 | grep -oE "silence_(start|end): [0-9.]+" > /tmp/s_$av.txt
  DUR=$DUR AV=$av python3 - <<'PY'
import json, subprocess, os
DUR=float(os.environ['DUR']); AV=os.environ['AV']; PAD=0.22
ev=[l.strip().split(': ') for l in open(f'/tmp/s_{AV}.txt')]
sil=[]; st=None
for k,v in ev:
    v=float(v)
    if k.endswith('start'): st=v
    elif st is not None: sil.append((st,v)); st=None
if st is not None: sil.append((st,DUR))
keep=[]; cur=0.0
for a,b in sil:
    a2=min(a+PAD,DUR); b2=max(b-PAD,0)
    if a2-cur>0.35: keep.append([round(cur,3),round(a2,3)])
    cur=max(cur,b2)
if DUR-cur>0.35: keep.append([round(cur,3),round(DUR,3)])
m=[keep[0]]
for a,b in keep[1:]:
    if a-m[-1][1]<0.12: m[-1][1]=b
    else: m.append([a,b])
d=f'/tmp/cut_{AV}'; os.makedirs(d,exist_ok=True); parts=[]
for i,(a,b) in enumerate(m):
    o=f'{d}/p{i:02d}.mp4'
    subprocess.run(['ffmpeg','-v','error','-ss',str(a),'-to',str(b),'-i',f'avatares/{AV}-bruto.mp4',
      '-c:v','libx264','-preset','medium','-crf','19','-pix_fmt','yuv420p','-r','30',
      '-c:a','aac','-b:a','192k','-ar','48000','-avoid_negative_ts','make_zero',o,'-y'],check=True)
    parts.append(o)
open(f'{d}/l.txt','w').write("\n".join(f"file '{p}'" for p in parts))
subprocess.run(['ffmpeg','-v','error','-f','concat','-safe','0','-i',f'{d}/l.txt','-c','copy',
  f'avatares/{AV}-cortado.mp4','-y'],check=True)
print(f'{AV}: {DUR:.1f}s -> {sum(b-a for a,b in m):.1f}s ({len(m)} cortes)')
PY
  IN=avatares/$av-cortado.mp4 OUT=avatares/CRIATIVO-$av.mp4 ./add-cta.sh >/dev/null
  rm -f avatares/$av-bruto.mp4 avatares/$av-cortado.mp4
  echo -n "  -> CRIATIVO-$av.mp4  "; ffprobe -v error -show_entries format=duration -of csv=p=0 avatares/CRIATIVO-$av.mp4
done
