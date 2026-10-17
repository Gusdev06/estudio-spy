# Monta a V3: legenda do gancho (f0-149, inclusive o chicote) + "his"->"her" na demo (f144-378).
import sys, subprocess, numpy as np, cv2
HERE='/Users/gustagoat/Documents/AIS-OS/projects/mentoria-spy/gram-detect/criativos/sarah-smith-1677505624160791-3var-2026-10-17/v3-quem-ele-curte'
sys.path.insert(0,HERE+'/scripts'); import comp, demo
SRC=HERE+'/../REFERENCIA-original.mp4'; OUT=HERE+'/pecas/v3-quem-ele-curte.mp4'
F0=cv2.imread(HERE+'/tmp/f0000.png').astype(np.int16)
def hook_copy(fr,dx):
    """substitui a caixa deslocada dx só onde o pixel ainda é a camada original (respeita o que estiver por cima)."""
    old=cv2.warpAffine(F0.astype(np.float32),np.float32([[1,0,dx],[0,1,0]]),(720,1280),flags=cv2.INTER_NEAREST).astype(np.int16)
    inter=cv2.warpAffine(comp.INT,np.float32([[1,0,dx],[0,1,0]]),(720,1280),flags=cv2.INTER_NEAREST).astype(bool)
    pix=inter & (np.abs(fr.astype(np.int16)-old).max(2)<40)
    # visibilidade por COLUNA (a camada é rígida e só é recortada na vertical pela borda do painel):
    # coluna com >=85% do interior batendo conta inteira; evita sobrar pixel antigo por ruído de compressão
    n=inter.sum(0); k=pix.sum(0); col=(n>0)&(k>=0.85*np.maximum(n,1))
    vis=inter & col[None,:]
    return comp.hook(fr,dx,0,vis)
def hook_dx(i): return 0 if i<140 else -12-48*(i-140)
def demo_dx(i): return 0 if i>=155 else 708-48*(i-140)
enc=subprocess.Popen(['ffmpeg','-hide_banner','-v','error','-y','-f','rawvideo','-pix_fmt','bgr24','-s','720x1280','-r','30','-i','-',
    '-i',SRC,'-map','0:v','-map','1:a','-vf','scale=out_color_matrix=bt709:out_range=tv:flags=accurate_rnd+full_chroma_int','-colorspace','bt709','-color_primaries','bt709','-color_trc','bt709','-color_range','tv','-c:v','libx264','-preset','slow','-crf','12','-pix_fmt','yuv420p','-r','30',
    '-c:a','copy','-movflags','+faststart',OUT],stdin=subprocess.PIPE)
log=[]
for i in range(1095):
    fr=cv2.imread(HERE+'/tmp/f%04d.png'%i)
    if i<150:
        d=hook_dx(i)
        for dx in ((d,) if i<140 else (d,d+720)): fr=hook_copy(fr,dx)
    if 144<=i<=378:
        fr=demo.patch(fr,demo_dx(i))
    enc.stdin.write(fr.tobytes())
enc.stdin.close(); enc.wait(); print('ok',enc.returncode)
