# Recria work/G.npy (original decodificado, 1822x1280x720x3 RGB, ~5 GB) usado por montar.py, flash.py e varredura.py. Rodar da pasta da peça.
import numpy as np, subprocess
mm = np.lib.format.open_memmap('work/G.npy', mode='w+', dtype=np.uint8, shape=(1822, 1280, 720, 3))
p = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', 'REFERENCIA-original.mp4', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], stdout=subprocess.PIPE)
for n in range(1822): mm[n] = np.frombuffer(p.stdout.read(1280 * 720 * 3), np.uint8).reshape(1280, 720, 3)
mm.flush()
