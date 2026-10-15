#!/bin/bash
# setup.sh — instala/verifica tudo que a esteira precisa. Uso: bash setup.sh [--testar]
set -u
ok(){ printf "  ✅ %s\n" "$1"; }; falta(){ printf "  ❌ %s — %s\n" "$1" "$2"; FALTOU=1; }
FALTOU=0; SO=$(uname -s)
echo "== 1. Ferramentas"
command -v ffmpeg >/dev/null && ok "ffmpeg $(ffmpeg -version | head -1 | cut -d' ' -f3)" || falta ffmpeg "brew install ffmpeg (Mac) · winget install Gyan.FFmpeg (Windows)"
command -v python3 >/dev/null && ok "python $(python3 -V | cut -d' ' -f2)" || falta python3 "brew install python"
command -v node >/dev/null && ok "node $(node -v)" || falta node "brew install node"
command -v wavespeed >/dev/null && ok "wavespeed CLI" || falta "wavespeed CLI" "npm i -g @wavespeed/cli && wavespeed login"
echo "== 2. Bibliotecas de Python"
for m in PIL numpy cv2; do python3 -c "import $m" 2>/dev/null && ok "$m" || falta "$m" "pip3 install pillow numpy opencv-python-headless"; done
echo "== 3. Transcrição"
if [ "$SO" = "Darwin" ] && [ "$(uname -m)" = "arm64" ]; then
  command -v uv >/dev/null && ok "uv (mlx-whisper roda sob demanda)" || falta uv "brew install uv"
else
  python3 -c "import faster_whisper" 2>/dev/null && ok "faster-whisper" || falta faster-whisper "pip3 install faster-whisper (e ver metodo/06-troubleshooting.md para o shim)"
fi
echo "== 4. Conta"
if command -v wavespeed >/dev/null; then
  wavespeed balance >/dev/null 2>&1 && ok "WaveSpeed logado ($(wavespeed balance 2>/dev/null | head -1))" || falta "login da WaveSpeed" "rode: wavespeed login"
fi
echo "== 5. Arquivos do pacote"
for f in metodo/01-regras.md scripts/checar-identidade.py scripts/face_detection_yunet_2023mar.onnx fontes/Poppins-Bold.ttf midia/ref-1-secret-revealed.mp4; do
  [ -e "$f" ] && ok "$f" || falta "$f" "descompacte os 3 zips na mesma pasta"
done
if [ "${1:-}" = "--testar" ]; then
  echo "== 6. Teste real (sem custo)"
  T=$(mktemp -d); ffmpeg -hide_banner -v error -f lavfi -i testsrc=size=720x1280:duration=2:rate=30 -pix_fmt yuv420p "$T/t.mp4" && ok "ffmpeg encoda"
  python3 -c "
from PIL import Image,ImageDraw,ImageFont;import numpy as np,cv2
f=ImageFont.truetype('fontes/Poppins-Bold.ttf',60);im=Image.new('RGB',(400,120));ImageDraw.Draw(im).text((10,20),'TESTE',font=f,fill='white')
d=cv2.FaceDetectorYN_create('scripts/face_detection_yunet_2023mar.onnx','',(320,320),0.6,0.3,5000)
print('  ✅ PIL + numpy + OpenCV/YuNet ok')" || falta "python" "reinstale as bibliotecas"
  rm -rf "$T"
fi
echo
[ "$FALTOU" = 0 ] && echo "Tudo pronto. Próximo passo: metodo/00-comeco-rapido.md" || echo "Resolva os ❌ acima e rode de novo."
