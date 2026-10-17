import numpy as np, cv2
HERE='/Users/gustagoat/Documents/AIS-OS/projects/mentoria-spy/gram-detect/criativos/sarah-smith-1677505624160791-3var-2026-10-17/v3-quem-ele-curte'
SIL=np.load(HERE+'/scripts/sil_f0.npy')
INT=cv2.erode(SIL,np.ones((9,9),np.uint8))  # 4px pra dentro: o anel da borda fica o original
TX=np.load(HERE+'/scripts/texto_novo.npy').astype(np.float32)/255  # RGBA
def shift(a,dx,dy):
    M=np.float32([[1,0,dx],[0,1,dy]])
    return cv2.warpAffine(a,M,(720,1280),flags=cv2.INTER_NEAREST,borderValue=0)
def hook(frame_bgr, dx=0, dy=0, colmask=None):
    """troca o texto da caixa: interior -> preto + texto novo, deslocado (dx,dy); colmask limita as colunas/pixels."""
    f=frame_bgr.astype(np.float32)
    inter=shift(INT,dx,dy).astype(bool)
    tx=shift(TX,dx,dy) if (dx or dy) else TX
    if colmask is not None: inter&=colmask
    a=tx[...,3]
    rgb=tx[...,2::-1]  # RGBA->BGR
    newpix=rgb*a[...,None]  # fundo preto
    f[inter]=newpix[inter]*255
    return np.clip(f+0.5,0,255).astype(np.uint8)
