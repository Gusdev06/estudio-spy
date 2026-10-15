#!/usr/bin/env python3
# Flora 959352790554428 (Zap, 360x640, 34,2 s) com a DUPLA e o ESTÚDIO novos (25/09). Layout de post sobre preto: faixa de título (y 44-150),
# JANELA DE VÍDEO 360x303 (y 168-470) e karaokê (y ~520-575) — faixa e karaokê ficam FORA da janela e saem do original intactos, assim como
# os painéis (n 267-884) e o áudio. Emendas por NÚMERO DE FRAME (30 fps): mulher n 0-116 · homem n 117-225 · mulher n 226-266 · painéis 267-884 · mulher 885-1025.
# n 263-266: light leak (transição de luz laranja) sobre a mulher original. Aqui a leak é lida nas faixas pretas em volta da janela e reaplicada
# sobre a mulher NOVA (ver leak()).
# Enquadramento: rosto (YuNet, maior score) do clipe escalado e posicionado no centro/altura medidos no original em cada bloco.
# Uso (de projects/mentoria-spy/): python3 .../montar.py <saida.mp4> [a1=a1-s7 b=b-s7 a2=a2-s7 a3=a3-s7]
import json, subprocess, sys, numpy as np, cv2
L='centerpag-detect/criativos/var10-flora-959352790554428-2026-09-27'; REF=f'{L}/REFERENCIA-original.mp4'
M='gram-detect/scripts/modelos/face_detection_yunet_2023mar.onnx'; OUT=sys.argv[1]; W,H,N=360,640,1026; WY0,WY1=168,471; WH=WY1-WY0
esc={'a1':'a1-s7','b':'b-s7','a2':'a2-s7','a3':'a3-s7'}; esc.update(dict(a.split('=') for a in sys.argv[2:]))
ALVO={'a1':(161.85,131.85,154.64),'b':(197.29,140.61,220.17),'a2':(160.45,126.01,157.64),'a3':(160.87,124.80,152.48)}  # mediana cx,cy,h do rosto no original (janela)
B=json.load(open(f'{L}/molde/blocos.json'))
def ler(arq,w,h,vf):
    raw=subprocess.run(['ffmpeg','-v','error','-i',arq,'-vf',vf+(',' if vf else '')+'scale=in_color_matrix=bt709:out_color_matrix=bt709,format=bgr24','-f','rawvideo','-'],capture_output=True).stdout
    return np.frombuffer(raw,np.uint8).reshape(-1,h,w,3)
O=ler(REF,W,H,'').copy(); assert len(O)==N, len(O)
def clipe(b):
    arq=f'{L}/clipes/{esc[b]}.mp4'
    cw,chh=[int(v) for v in subprocess.run(['ffprobe','-v','error','-select_streams','v','-show_entries','stream=width,height','-of','csv=p=0',arq],capture_output=True,text=True).stdout.strip().split(',')]
    f=ler(arq,cw,chh,'trim=start_frame=1,setpts=PTS-STARTPTS,fps=30')   # 1º frame da Pruna descartado (padrão dos lotes anteriores)
    det=cv2.FaceDetectorYN_create(M,'',(cw,chh),0.86,0.3,5000); r=[]
    for x in f[::3]:
        d=det.detect(np.ascontiguousarray(x))[1]
        if d is not None and len(d): a=max(d,key=lambda q:q[-1]); r.append((a[0]+a[2]/2,a[1]+a[3]/2,a[3]))
    cx,cy,h=np.median(np.array(r),axis=0); tx,ty,th=ALVO[b]; s=max(th/h,W/cw,WH/chh)
    sw,sh=int(round(cw*s)),int(round(chh*s)); x=int(min(max(cx*s-tx,0),sw-W)); y=int(min(max(cy*s-ty,0),sh-WH))
    print(f'{b} ({esc[b]}): {len(f)} fr, escala {s:.3f}, crop x{x} y{y}')
    return [cv2.resize(fr,(sw,sh),interpolation=cv2.INTER_LANCZOS4)[y:y+WH,x:x+W] for fr in f]
LEAK=range(263,267)   # n 262 ainda está limpo; a leak começa no 263 e o painel entra no 267
def leak(n,novo):
    # modelo por canal: out = k·base + add(x,y). add = a própria leak, lida onde a base é PRETA (faixas pretas logo acima, y 152-166, e logo abaixo,
    # y 476-515, da janela) e interpolada na vertical por coluna — não tem nada da mulher original. k = 1 escalar por canal (escurecimento/tinta),
    # ajustado por mínimos quadrados contra a mulher original do n 262. Aplicado à mulher nova: out = k·nova + add.
    f=O[n].astype(np.float32); cima=f[152:167].mean(0); baixo=f[476:516].mean(0)   # (360,3)
    cima=cv2.GaussianBlur(cima[None],(0,0),6)[0]; baixo=cv2.GaussianBlur(baixo[None],(0,0),6)[0]
    t=((np.arange(WY0,WY1)-159)/(495-159))[:,None,None]; add=cima[None]*(1-t)+baixo[None]*t
    base=O[262,WY0:WY1].astype(np.float32); r=f[WY0:WY1]-add
    k=np.clip((r*base).sum((0,1))/(base*base).sum((0,1)),0,1.2)
    return np.clip(k*novo.astype(np.float32)+add,0,255).astype(np.uint8)
for b,d in B.items():
    c=clipe(b); f0,f1=d['f0'],d['f1']; assert len(c)>=f1-f0+1, (b,len(c))
    for n in range(f0,f1+1):
        novo=c[n-f0]
        if n in LEAK:
            novo=leak(n,novo)
        O[n,WY0:WY1]=novo
p=subprocess.Popen(['ffmpeg','-hide_banner','-v','error','-y','-f','rawvideo','-pix_fmt','bgr24','-s',f'{W}x{H}','-r','30','-i','-','-i',REF,
   '-map','0:v','-map','1:a','-c:a','copy','-vf','scale=in_color_matrix=bt709:out_color_matrix=bt709,format=yuv420p','-c:v','libx264','-preset','slow','-crf','16',
   '-colorspace','bt709','-color_primaries','bt709','-color_trc','bt709','-color_range','tv','-movflags','+faststart',OUT],stdin=subprocess.PIPE)
p.stdin.write(O.tobytes()); p.stdin.close(); assert p.wait()==0; print('ok ->',OUT)
