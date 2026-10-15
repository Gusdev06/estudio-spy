#!/bin/bash
# Transcreve o áudio de um vídeo local usando o reconhecimento de fala ON-DEVICE da Apple.
# Nada sai da máquina. Requer só Xcode Command Line Tools (swiftc) — sem ffmpeg, sem brew, sem API.
#
#   ./transcrever.sh caminho/video.mp4 [en-US|pt-BR]
#
# Notas de armadilha (custaram tempo, não repita):
#  - swift interpretado (`swift x.swift`) CRASHA no TCC: precisa ser um .app com
#    NSSpeechRecognitionUsageDescription no Info.plist e assinado (codesign -s -).
#  - bloquear a main thread com semáforo trava o SFSpeechRecognizer: use RunLoop.main.run().
set -euo pipefail
VIDEO="$1"; LOC="${2:-en-US}"
DIR="$(cd "$(dirname "$0")" && pwd)"
BUILD="$DIR/.build"; APP="$BUILD/GramSTT.app"   # caminho FIXO: a permissao de Reconhecimento de Fala
                                              # e concedida por app+caminho; em pasta temporaria o macOS
                                              # pede autorizacao de novo a cada rodada e trava.
mkdir -p "$BUILD"
BASE="$(basename "${VIDEO%.*}")"
OUT="$(dirname "$VIDEO")/$BASE-stt.txt"

afconvert -f WAVE -d LEI16@16000 -c 1 "$VIDEO" "$BUILD/a.wav"

mkdir -p "$APP/Contents/MacOS"
cat > "$APP/Contents/Info.plist" <<'PLIST'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0"><dict>
<key>CFBundleExecutable</key><string>GramSTT</string>
<key>CFBundleIdentifier</key><string>local.gusta.gramstt</string>
<key>CFBundleName</key><string>GramSTT</string>
<key>CFBundlePackageType</key><string>APPL</string>
<key>LSUIElement</key><true/>
<key>NSSpeechRecognitionUsageDescription</key><string>Transcrever o audio de um video local de anuncio.</string>
</dict></plist>
PLIST
if [ ! -x "$APP/Contents/MacOS/GramSTT" ] || [ "$DIR/transcrever-stt.swift" -nt "$APP/Contents/MacOS/GramSTT" ]; then
  swiftc "$DIR/transcrever-stt.swift" -o "$APP/Contents/MacOS/GramSTT"
  codesign -f -s - "$APP"
fi

rm -f "$OUT"
open "$APP" --args --in "$BUILD/a.wav" --loc "$LOC" --out "$OUT"
for _ in $(seq 1 120); do
  grep -q "=== TEXTO ===\|ERR \|AUTH_DENIED\|TIMEOUT" "$OUT" 2>/dev/null && break
  sleep 2
done
grep -v '^PARTIAL ' "$OUT" > "$OUT.tmp" && mv "$OUT.tmp" "$OUT"
echo "-> $OUT"
sed -n '/=== TEXTO ===/,/=== SEGMENTOS ===/p' "$OUT"
