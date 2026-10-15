#!/usr/bin/env python3
# Confere cada clipe Pruna nos 3 defeitos vistos no g1 (24/09): moldura/"foto no papel" (borda clara numa cena escura),
# gente entrando pelas bordas laterais (mudança nas faixas de 70 px vs o 1º frame) e 2º rosto (YuNet, score >= 0,86: o vaso da estante dá 0,80).
# Uso (de projects/mentoria-spy/): python3 .../checar.py g1 [g2 …]
import subprocess, sys, numpy as np, cv2
L='gram-detect/criativos/podcast-gram-clone-avatares-2026-09-24'; M='gram-detect/scripts/modelos/face_detection_yunet_2023mar.onnx'
ruim=0
for k in sys.argv[1:]:
    for b in ['a1','b','a2','a3']:
        c=f'{L}/{k}/clipes/{b}.mp4'
        raw=subprocess.run(['ffmpeg','-v','error','-i',c,'-vf','fps=6','-f','rawvideo','-pix_fmt','bgr24','-'],capture_output=True).stdout
        f=np.frombuffer(raw,np.uint8).reshape(-1,1024,896,3); g=f.mean(3)
        borda=np.array([max(x[:10].mean(),x[-10:].mean(),x[:,:10].mean(),x[:,-10:].mean()) for x in g])
        lat=np.array([max(np.abs(x[:, :70]-g[0][:, :70]).mean(),np.abs(x[:,-70:]-g[0][:,-70:]).mean()) for x in g])
        det=cv2.FaceDetectorYN_create(M,'',(896,1024),0.86,0.3,5000)   # 0,8 contava o vaso da estante (score 0,80)
        rostos=[0 if d is None else len(d) for d in (det.detect(np.ascontiguousarray(x))[1] for x in f)]
        prob=[]
        if borda.max()>110: prob.append(f'moldura em {np.argmax(borda>110)/6:.1f}s (borda {borda.max():.0f})')
        if lat.max()>28: prob.append(f'borda lateral mexe em {np.argmax(lat>28)/6:.1f}s ({lat.max():.0f})')
        if max(rostos)>1: prob.append(f'{max(rostos)} rostos em {rostos.index(max(rostos))/6:.1f}s')
        if min(rostos)==0: prob.append(f'sem rosto em {rostos.index(0)/6:.1f}s')
        ruim+=bool(prob); print(k,b,'OK' if not prob else 'PROBLEMA: '+'; '.join(prob),f'(borda máx {borda.max():.0f}, lateral máx {lat.max():.0f})')
sys.exit(1 if ruim else 0)
