import subprocess,sys,json,numpy as np,cv2
D=sys.argv[1]; r=json.load(open(f'{D}/conferencia/varredura.json')); ns=[int(x[0]) for x in sorted(r,key=lambda z:-z[1])[:1]]+[300,1100]
def fr(p,n): return np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',p,'-vf',f'select=eq(n\\,{n})','-vsync','0','-frames:v','1','-f','rawvideo','-pix_fmt','bgr24','-'],capture_output=True).stdout,np.uint8).reshape(720,960,3)
rows=[]
for n in ns:
    o,p=fr(f'{D}/REFERENCIA-original.mp4',n),fr(f'{D}/pecas/variacao.mp4',n); eq=np.abs(o.astype(int)-p.astype(int)).max(2)<8
    m=p.copy(); m[eq]=(0,0,255)
    r_=np.hstack([cv2.resize(x,(480,360)) for x in (o,p,m)]); cv2.putText(r_,f'n{n} (vermelho = pixel igual ao original)',(8,28),0,0.8,(0,255,255),2); rows.append(r_)
cv2.imwrite(f'{D}/conferencia/iguais-ao-original.jpg',np.vstack(rows),[cv2.IMWRITE_JPEG_QUALITY,82])
