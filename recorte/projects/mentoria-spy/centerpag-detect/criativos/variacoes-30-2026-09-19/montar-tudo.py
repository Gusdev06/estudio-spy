#!/usr/bin/env python3
# Monta as variações já com clipe pronto (custo zero), uma por vez: varredura do clipe → peça → cópia em CRIATIVOS-PRONTOS → linha no LEIA-ME.
#   secret sNN → remontar-secret.sh (molde do Secret Revealed)      · luiza lNN → luiza-troca-avatar-android/montar.py (look Android)
#   podcast pNN → CLIPES=…/pNN/clipes montar-clone.py (5 blocos)
# Uso (de projects/mentoria-spy/): python3 montar-tudo.py [secret|luiza|podcast] [ids…]   (sem ids = todos com clipe e sem peça)
import os, subprocess, sys, csv
V='centerpag-detect/criativos/variacoes-30-2026-09-19'; P='centerpag-detect/criativos/podcast-wpp-clone-avatares-2026-09-13'
SEC='centerpag-detect/criativos/zap-secret-revealed-avatar-2026-09-10/remontar-secret.sh'; LUI='centerpag-detect/criativos/luiza-troca-avatar-android-2026-09-19/montar.py'
NUM0={'secret':71,'luiza':81,'podcast':91}   # numeração em CRIATIVOS-PRONTOS: 71-80 secret · 81-90 luiza · 91-100 podcast
lote=sys.argv[1]; ids=sys.argv[2:]
cast={r[0]:r[1] for r in csv.reader(open(f'{V}/{lote}/casting.tsv'),delimiter='\t')}
if not ids: ids=sorted(cast)
def varre(clip,out,n=24):
    subprocess.run(['ffmpeg','-hide_banner','-v','error','-y','-i',clip,'-vf',f"select='not(mod(n,{max(1,int(24*30/n))}))',scale=90:-1,tile={n}x1",'-vsync','0','-frames:v','1',out],check=True)
for vid in ids:
    i=int(vid[1:]); num=NUM0[lote]+i-1; slug=cast[vid]; out=f'{V}/{lote}/pecas/{vid}-{slug}.mp4'
    if lote=='podcast':
        cl=f'{P}/{vid}/clipes'
        if not all(os.path.exists(f'{cl}/bloco-{b}b.mp4') for b in range(1,6)): print('sem clipes',vid); continue
        for b in range(1,6): varre(f'{cl}/bloco-{b}b.mp4',f'{V}/{lote}/conferencia/{vid}-bloco{b}.jpg',12)
        subprocess.run(['python3',f'{P}/montar-clone.py',out],env={**os.environ,'CLIPES':cl},check=True,capture_output=True)
        pref='ZAP-podcast-wpp-clone'
    else:
        clip=f'{V}/{lote}/clipes/{vid}.mp4'
        if not os.path.exists(clip): print('sem clipe',vid); continue
        varre(clip,f'{V}/{lote}/conferencia/{vid}-varredura.jpg')
        if lote=='secret': subprocess.run(['bash',SEC,clip,out],check=True,capture_output=True); pref='ZAP-secret-revealed'
        else: subprocess.run(['python3',LUI,clip,out],check=True,capture_output=True); pref='ZAP-luiza-split-look-android'
    fr=subprocess.run(['ffprobe','-v','error','-show_entries','stream=nb_frames','-of','csv=p=0',out],capture_output=True,text=True).stdout.split()[0]
    dst=f'CRIATIVOS-PRONTOS/{num}-{pref}-{slug}.mp4'; subprocess.run(['cp',out,dst],check=True)
    p='CRIATIVOS-PRONTOS/LEIA-ME.md'; s=open(p).read()
    if f'| {num} |' not in s:
        base={'secret':'Secret Revealed (22) com outro avatar','luiza':'Luiza split (64) com outra avatar, look Android','podcast':'podcast WPP clone (40) com outro par de avatares'}[lote]
        row=f'| {num} | {pref}-{slug} | Spy Zap | {base}: {slug.replace("-"," ")} — só rosto/roupa mudam; áudio e edição do original | {V}/{lote}/pecas |\n'
        # insere logo depois da última linha numerada da tabela principal (antes de '### 12/09')
        k=s.index('\n### 12/09'); s=s[:k]+'\n'+row.rstrip('\n')+s[k:]
        open(p,'w').write(s)
    print(f'ok {vid} → {dst} ({fr} fr)')
