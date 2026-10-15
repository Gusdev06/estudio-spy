#!/usr/bin/env python3
# montar-var.py vN [vM …] — variação do podcast Zap (versão 06 = funil nos splits + música) trocando SÓ a cena 1 e o texto da caixa.
# Cena 1 = var5/clipes/cena-1-vN.mp4 (H3 768p, close host, com áudio) cortada no fim da fala + 0,3 s e com pausas ≥ 0,4 s reduzidas a 0,25 s
# (mesma regra de molde/timeline.py); cenas 2–7, funil, setas e música iguais; karaokê da cena 1 do whisper do clipe novo; caixa com o texto de
# var5/hooks.tsv (auto-fit da fonte em 2 linhas). Saída var5/PODCAST-ZAP-vN-<slug>.mp4. Uso (de projects/mentoria-spy/): python3 var5/montar-var.py v1 v2 …
import json, os, re, subprocess, sys, unicodedata
from PIL import ImageFont
P='gram-detect/criativos/podcast-hook-polemico-2026-09-05'; V=f'{P}/var5'; FPS=30
REC='EDIÇÃO 3/EDIÇAO ANIMADA/ScreenRecording_08-13-2026 19-56-53_1.MP4'; MUSICA=f'{P}/audio/musica-7y4kJtkioFk.m4a'
FP='gram-detect/scripts/fonts/Poppins-Bold.ttf'; FI='gram-detect/scripts/fonts/Inter-Bold.ttf'
RESP,PMAX,PKEEP=0.3,0.4,0.25
T0=json.load(open(f'{P}/molde/timeline.json')); SC0=T0['scenes']
hooks={c[0]:(c[1],c[2]) for c in (l.rstrip('\n').split('\t') for l in open(f'{V}/hooks.tsv')) if len(c)>=3 and not c[0].startswith('#')}
def slug(t): t=unicodedata.normalize('NFKD',t).encode('ascii','ignore').decode().lower(); return re.sub(r'-+','-',re.sub(r"[^a-z0-9]+",'-',t)).strip('-')
def silences(c):
    r=subprocess.run(['ffmpeg','-nostdin','-v','info','-i',c,'-af',f'silencedetect=n=-35dB:d={PMAX}','-f','null','-'],capture_output=True,text=True).stderr
    st=[float(x) for x in re.findall(r'silence_start: ([\d.]+)',r)]; en=[float(x) for x in re.findall(r'silence_end: ([\d.]+)',r)]
    return list(zip(st,en+[9e9]*(len(st)-len(en))))
def norm(w): return re.sub(r"[^a-z0-9']","",w.lower().replace('’',"'"))
def whisper(clip,js):
    if os.path.exists(js): return
    wav=js[:-5]+'-16k.wav'; subprocess.run(['ffmpeg','-nostdin','-v','error','-y','-i',clip,'-ac','1','-ar','16000',wav],check=True)
    subprocess.run(['uvx','--from','mlx-whisper','mlx_whisper',wav,'--model','mlx-community/whisper-small.en-mlx','--word-timestamps','True','--output-dir',os.path.dirname(js),'--output-format','json','--language','en'],check=True,capture_output=True)
    os.rename(wav[:-4]+'.json',js); os.remove(wav)
def blocos_fala(fala):
    # 2–3 palavras por bloco: quebra em pontuação; pedaço com >3 palavras é dividido ao meio
    out=[]
    for ch in re.split(r'[,.;:!?…]+|\s—\s',fala):
        ws=[w for w in ch.split() if norm(w)]
        while len(ws)>3: k=(len(ws)+1)//2; out.append(' '.join(ws[:k])); ws=ws[k:]
        if ws: out.append(' '.join(ws))
    return [re.sub(r'^["“”\']+|["“”\']+$','',b).lower() for b in out]
def caixa_lines(txt):
    if '|' in txt: return txt.split('|')[:2]
    ws=txt.split(); best=None
    for i in range(1,len(ws)):
        a,b=' '.join(ws[:i]),' '.join(ws[i:]); d=abs(len(a)-len(b))
        if best is None or d<best[0]: best=(d,[a,b])
    return best[1] if best else [txt,'']
for vid in sys.argv[1:]:
    caixa,fala=hooks[vid]; clip=f'{V}/clipes/cena-1-{vid}.mp4'; js=f'{V}/audio/clip-cena-1-{vid}.json'; whisper(clip,js)
    words=[(norm(w['word']),w['start'],w['end']) for s in json.load(open(js))['segments'] for w in s['words']]; words=[w for w in words if w[0]]
    cd=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',clip],capture_output=True,text=True).stdout)
    wend=words[-1][2]; fim=min(wend+RESP,cd); removed=[]
    for a,b in silences(clip):
        b=min(b,cd)
        if a<0.05 and b>0.25 and b<wend: removed.append((0.1,round(b-0.05,3)))
        elif a>0.05 and b<=wend+0.05 and (b-a)>=PMAX: removed.append((round(a+PKEEP,3),round(b,3)))
    removed=[r for r in removed if r[1]-r[0]>0.05]; segs=[]; cur=0.0
    for a,b in removed:
        if a>cur: segs.append((cur,a))
        cur=b
    if fim>cur: segs.append((cur,fim))
    frames=[max(1,int(round((e-s)*FPS))) for s,e in segs]; n1=sum(frames)
    sc1={'cena':1,'clip':clip,'segments':[[s,e] for s,e in segs],'seg_frames':frames,'removed':removed,'out_start':0,'out_frames':n1}
    delta=n1-SC0[0]['out_frames']; SC=[sc1]
    for s in SC0[1:]: s=dict(s); s['out_start']+=delta; SC.append(s)
    TOTAL=SC[-1]['out_start']+SC[-1]['out_frames']
    S=lambda i:SC[i-1]['out_start']; E=lambda i:SC[i-1]['out_start']+SC[i-1]['out_frames']
    BOX_END=E(2); SETAS_INI=TOTAL-90
    print(f'{vid}: fala até {wend:.2f}s, corta em {fim:.2f}s de {cd:.2f}s, pausas {removed} → cena 1 = {n1} fr ({n1/FPS:.2f}s, era {SC0[0]["out_frames"]}) · total {TOTAL} fr = {TOTAL/FPS:.2f}s')
    # ---- karaokê: cena 1 do whisper novo; cenas 2–7 do molde, deslocadas ----
    def to_out(t):
        rem=0.0
        for a,b in removed:
            if t>=b: rem+=b-a
            elif t>a: rem+=t-a
        return int(round((t-rem)*FPS))
    kar=[]; k=0; times=[]; bl=blocos_fala(fala)
    for b in bl:
        st=en=None
        for t in [norm(x) for x in b.split()]:
            j=k
            while j<len(words) and not (words[j][0]==t or words[j][0].startswith(t) or t.startswith(words[j][0])): j+=1
            if j>=len(words): print(f'  AVISO {vid}: "{t}" não achada no whisper',file=sys.stderr); break
            if st is None: st=words[j][1]
            en=words[j][2]; k=j+1
        if st is None: st=times[-1][1] if times else 0.0; en=st+0.4
        times.append((st,en))
    for n,(b,(st,en)) in enumerate(zip(bl,times)):
        f0=to_out(st); f1=(to_out(times[n+1][0])-3) if n+1<len(times) else min(to_out(en)+6,n1)
        kar.append((f0,max(f1,f0+2),b))
    for l in open(f'{P}/molde/karaoke.tsv'):
        if l.startswith('#') or not l.strip(): continue
        a,b,st,txt=l.rstrip('\n').split('\t')[:4]
        if int(a)>=SC0[1]['out_start']: kar.append((int(a)+delta,int(b)+delta,txt))
    os.makedirs(f'{V}/molde/k-{vid}',exist_ok=True)
    with open(f'{V}/molde/karaoke-{vid}.tsv','w') as f:
        f.write('# frame_ini\tframe_fim(excl)\ttexto\n'); [f.write(f'{a}\t{b}\t{t}\n') for a,b,t in kar]
    json.dump({'fps':FPS,'total_frames':TOTAL,'scenes':SC},open(f'{V}/molde/timeline-{vid}.json','w'),indent=1)
    # ---- caixa: 2 linhas, Poppins Bold 60 ou menor até caber em 828 px ----
    L1,L2=caixa_lines(caixa.upper()); size=60
    while size>36 and max(ImageFont.truetype(FP,size).getlength(x) for x in (L1,L2))>828: size-=2
    pitch=round(74*size/60); cap=round(42*size/60); top1=round(95-(pitch+cap)/2); top2=top1+pitch
    print(f'  caixa: "{L1}" / "{L2}" · Poppins Bold {size} · topos {top1}/{top2}')
    esc=lambda s:s.replace("'","’").replace(':','\\:').replace('%','\\%')
    # ---- grafo (igual ao montar-funil.py, com a cena 1 nova) ----
    inputs=[]; fc=[]; vs=[]; as_=[]
    for idx,sc in enumerate(SC):
        inputs+=['-i',sc['clip']]; kk=len(sc['segments'])
        fc.append(f"[{idx}:v]split={kk}"+''.join(f'[v{idx}_{j}]' for j in range(kk))+';'); fc.append(f"[{idx}:a]asplit={kk}"+''.join(f'[a{idx}_{j}]' for j in range(kk))+';')
        for j,((s,e),fr) in enumerate(zip(sc['segments'],sc['seg_frames'])):
            fc.append(f"[v{idx}_{j}]trim=start={s}:end={e},setpts=PTS-STARTPTS,scale=1080:1920:force_original_aspect_ratio=increase:flags=lanczos,crop=1080:1920,fps={FPS},tpad=stop_mode=clone:stop_duration=2,trim=end_frame={fr},setpts=PTS-STARTPTS,format=yuv420p[sv{idx}_{j}];")
            fc.append(f"[a{idx}_{j}]atrim=start={s}:end={e},asetpts=PTS-STARTPTS,aformat=sample_rates=44100:channel_layouts=stereo,apad,atrim=end_sample={fr*1470},asetpts=PTS-STARTPTS[sa{idx}_{j}];")
            vs.append(f'[sv{idx}_{j}]'); as_.append(f'[sa{idx}_{j}]')
    fc.append(''.join(v+a for v,a in zip(vs,as_))+f'concat=n={len(vs)}:v=1:a=1[base][voz];')
    NS=len(SC); inputs+=['-i',MUSICA]   # NS = música
    fc.append(f"[{NS}:a]aformat=sample_rates=44100:channel_layouts=stereo,atrim=end={TOTAL/FPS:.3f},volume=0.09,afade=t=in:st=0:d=1,afade=t=out:st={TOTAL/FPS-2.5:.3f}:d=2.5[mus];[voz][mus]amix=inputs=2:normalize=0:duration=first[aout];")
    SPLIT={3:440,6:286,7:400}; KY_SPLIT=890; KY_FULL=1472; PY=960
    ysel=f"if(lt(n\\,{S(4)})\\,{SPLIT[3]}\\,if(lt(n\\,{S(7)})\\,{SPLIT[6]}\\,{SPLIT[7]}))"
    en_split=f"between(n\\,{S(3)}\\,{E(3)-1})+between(n\\,{S(6)}\\,{E(6)-1})+gte(n\\,{S(7)})"
    fc.append(f"[base]split=2[b0][bt];[bt]crop=1080:960:0:'{ysel}'[top];[b0][top]overlay=0:0:eof_action=pass:enable='{en_split}'[v0];")
    FA,FB,FC1=65,34,4; FC2=SC[5]['out_frames']-FA-FB-FC1
    n_in=NS+1
    for ss,t in [(0,2.3),(2.0,5.1),(7.0,0.2),(23.6,2.95),(116.0,5.6)]: inputs+=['-ss',str(ss),'-t',str(t),'-i',REC]
    inputs+=['-loop','1','-framerate',str(FPS),'-t','4','-i',f'{P}/molde/painel-fim-188.05.png']
    R=lambda k:n_in+k   # 0..4 = trechos da gravação, 5 = frame congelado
    CROP_MAPA='1170:1040:0:1110'; CROP_FORM='1150:1022:10:110'; CROP_FIM='1170:1040:0:960'
    BLUR="split=2[bl0][bl1];[bl1]crop=340:178:690:633,boxblur=22:2[blb];[bl0][blb]overlay=690:633,"
    def panel(src,crop,extra,frames,start,name):
        fc.append(f"[{src}]{extra}crop={crop},scale=1080:960:flags=lanczos,fps={FPS},tpad=stop_mode=clone:stop_duration=4,trim=end_frame={frames},setpts=PTS-STARTPTS,format=rgba,tpad=start_duration={start/FPS:.4f}:start_mode=add:color=0x00000000[{name}];")
    panel(f'{R(4)}:v',CROP_MAPA,'',E(3)-S(3),S(3),'p3')
    fc.append(f"[{R(0)}:v]crop={CROP_FORM},scale=1080:960:flags=lanczos,fps={FPS},trim=end_frame={FA},setpts=PTS-STARTPTS[p6a];")
    fc.append(f"[{R(1)}:v]{BLUR}crop={CROP_FORM},scale=1080:960:flags=lanczos,setpts=PTS/4.4,fps={FPS},trim=end_frame={FB},setpts=PTS-STARTPTS[p6b];")
    fc.append(f"[{R(2)}:v]{BLUR}crop={CROP_FORM},scale=1080:960:flags=lanczos,fps={FPS},tpad=stop_mode=clone:stop_duration=1,trim=end_frame={FC1},setpts=PTS-STARTPTS[p6c1];")
    fc.append(f"[{R(3)}:v]crop={CROP_MAPA},scale=1080:960:flags=lanczos,fps={FPS},tpad=stop_mode=clone:stop_duration=1,trim=end_frame={FC2},setpts=PTS-STARTPTS[p6c2];")
    fc.append(f"[p6a][p6b][p6c1][p6c2]concat=n=4:v=1:a=0,format=rgba,tpad=start_duration={S(6)/FPS:.4f}:start_mode=add:color=0x00000000[p6];")
    panel(f'{R(5)}:v',CROP_FIM,'',E(7)-S(7),S(7),'p7')
    fc.append(f"[v0][p3]overlay=x=0:y={PY}:eof_action=pass:enable='between(n,{S(3)},{E(3)-1})'[v1];[v1][p6]overlay=x=0:y={PY}:eof_action=pass:enable='between(n,{S(6)},{E(6)-1})'[v2];[v2][p7]overlay=x=0:y={PY}:eof_action=pass:enable='gte(n,{S(7)})'[v3];")
    fc.append(f"color=c=0xFE0553:s=868x197:r={FPS}:d={BOX_END/FPS+1:.2f},format=rgb24,"
     f"drawtext=fontfile={FP}:fontsize={size}:fontcolor=0x2C040A:borderw=2:bordercolor=0x2C040A:text='{esc(L1)}':x=(w-text_w)/2+5:y={top1+5},"
     f"drawtext=fontfile={FP}:fontsize={size}:fontcolor=0x2C040A:borderw=2:bordercolor=0x2C040A:text='{esc(L2)}':x=(w-text_w)/2+5:y={top2+5},"
     f"drawtext=fontfile={FP}:fontsize={size}:fontcolor=0xEEFC00:borderw=2:bordercolor=0x2C040A:text='{esc(L1)}':x=(w-text_w)/2:y={top1},"
     f"drawtext=fontfile={FP}:fontsize={size}:fontcolor=0xEEFC00:borderw=2:bordercolor=0x2C040A:text='{esc(L2)}':x=(w-text_w)/2:y={top2},"
     f"scale=out_color_matrix=bt709:out_range=tv,format=yuv420p[caixa];[v3][caixa]overlay=x=106:y=862:eof_action=pass:enable='lt(n,{BOX_END})'[v4];")
    inputs+=['-framerate',str(FPS),'-i',f'{P}/setas/%03d.png']; SI=R(6)
    fc.append(f"[{SI}:v]format=rgba,loop=loop=2:size=94:start=0,tpad=start_duration={SETAS_INI/FPS:.4f}:start_mode=add:color=0x00000000[setas];[v4][setas]overlay=x=340:y=1290:eof_action=pass:enable='gte(n,{SETAS_INI})'[v5];")
    def split_at(f): return (S(3)<=f<E(3)) or (S(6)<=f<E(6)) or f>=S(7)
    dt=[]
    for i,(a,b,txt) in enumerate(kar):
        p=f'{V}/molde/k-{vid}/{i:02d}.txt'; open(p,'w').write(txt); y=KY_SPLIT if split_at(a) else KY_FULL
        c=f"drawtext=fontfile={FI}:textfile={p}:fontsize=69:x=(w-text_w)/2:y={y}:enable='between(n\\,{a}\\,{b-1})'"
        dt.append(f"{c}:fontcolor=0x000000@0.0:borderw=9:bordercolor=0x000000@0.35"); dt.append(f"{c}:fontcolor=0xFCFCFC:borderw=4:bordercolor=0x0C0B0C@0.95")
    fc.append('[v5]'+','.join(dt)+'[v]')
    OUT=f'{V}/PODCAST-ZAP-{vid}-{slug(caixa)}.mp4'
    cmd=['ffmpeg','-nostdin','-v','error','-y']+inputs+['-filter_complex',''.join(fc),'-map','[v]','-map','[aout]','-frames:v',str(TOTAL),'-t',f'{TOTAL/FPS:.4f}',
     '-c:v','libx264','-preset','slow','-crf','16','-pix_fmt','yuv420p','-colorspace','bt709','-color_primaries','bt709','-color_trc','bt709','-color_range','tv','-c:a','aac','-b:a','192k','-movflags','+faststart',OUT]
    open(f'{V}/molde/ultimo-comando-{vid}.txt','w').write(' '.join(cmd)); subprocess.run(cmd,check=True); print('  ok ->',OUT)
