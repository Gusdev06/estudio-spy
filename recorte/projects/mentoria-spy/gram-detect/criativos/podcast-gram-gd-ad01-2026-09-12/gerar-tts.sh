#!/bin/bash
# TTS das 7 falas do podcast Gram (MiniMax speech-2.6-hd; host Wise_Woman, convidada Calm_Woman — as vozes da peça 06 do Zap). ≈ US$ 0,05.
set -e; cd "$(dirname "$0")/../../.."; N=gram-detect/criativos/podcast-gram-gd-ad01-2026-09-12
tts(){ wavespeed run minimax/speech-2.6-hd -i "text=$3" -i "voice_id=$2" -i language_boost=English --json --download "$N/audio/$1.mp3" > "$N/audio/$1.json" 2> "$N/audio/$1.log"; echo "ok $1"; }
tts host-1  Wise_Woman "There's a detail on Instagram that gives almost everyone away." &
tts guest-2 Calm_Woman "Yeah. I found something I wasn't even looking for. I didn't touch their phone. I just typed the username." &
tts guest-3 Calm_Woman "Whoever hides something leaves small traces. Messages, contacts, strange behavior. Even what they think they deleted." &
tts host-4  Wise_Woman "You don't need to guess. You don't need to argue. You don't need to grab their phone." &
tts guest-5 Calm_Woman "You just need to know where to look." &
tts host-6  Wise_Woman "There's a tool that shows it in seconds. You type the username. Nothing goes to their phone. The first check is free." &
tts host-7  Wise_Woman "The access is right below, while this tool is still available." &
wait
