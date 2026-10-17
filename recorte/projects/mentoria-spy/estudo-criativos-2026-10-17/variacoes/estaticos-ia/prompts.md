# Prompts — estáticos IA (17/10/2026)

Modelo: `openai/gpt-image-2/edit` (WaveSpeed), resolution 1k, quality medium (primeira tentativa).
Ref A = `tryfidelo-2026-10-17/anuncios/megan-rodriguez-1559475625325895.jpg` (2:3)
Ref B = `tryfidelo-2026-10-17/anuncios/silvia-amorin-2007437113276299.jpg` (4:5)

## 1a-she-deleted (A, aspect 2:3)
```
Edit this ad image. Keep EXACTLY the same layout, composition, neon pink/purple color palette, fonts, icons, timeline, chat phone mockup, list and bottom button. Make only these changes:
1. Replace the man looking at his phone with a woman (late 20s, dark hair) in the same pose, same position, same dark room and same moody neon lighting, looking anxiously at her phone late at night.
2. Headline text must read exactly: "SHE DELETED" (white) / "THE EVIDENCE." (pink), then "OR AT LEAST" (white) / "SHE THOUGHT SHE DID." (pink).
3. Middle headline must read exactly: "SEE WHAT SHE" (white) / "TRIED TO ERASE." (pink).
4. In the chat mockup header, the contact name reads exactly "Her" with the heart, instead of "Him". The chat photo shows a man instead of a woman.
All other text stays exactly as in the original: "2:14 AM Private DM", "2:37 AM Photo sent", "2:41 AM Message deleted", "2:46 AM Photo deleted", "Private conversations", "Deleted messages", "Deleted photos", "THE DIGITAL FOOTPRINT DOESN'T LIE.", "Tap the button below", "Can't stop thinking about you...", "This message was deleted", "Photo removed", "Message deleted", "Active now". Spell every word correctly. No logos, no brand names.
```

## 1b-he-deleted-dms (A, aspect 2:3)
```
Edit this ad image. Keep EVERYTHING exactly the same — same man, same pose, same layout, colors, fonts, icons, timeline, chat phone mockup, list and bottom button. Change ONLY the top headline, which must read exactly: "HE DELETED" (white) / "THE DMs." (pink, capital D, capital M, lowercase s), then "OR AT LEAST" (white) / "HE THOUGHT HE DID." (pink). All other text stays exactly as in the original, spelled correctly: "2:14 AM Private DM", "2:37 AM Photo sent", "2:41 AM Message deleted", "2:46 AM Photo deleted", "SEE WHAT HE TRIED TO ERASE.", "Private conversations", "Deleted messages", "Deleted photos", "THE DIGITAL FOOTPRINT DOESN'T LIE.", "Tap the button below", "Him", "Active now", "Can't stop thinking about you...", "This message was deleted", "Photo removed", "Message deleted". No logos, no brand names.
```

## 1c-clone-novo-rosto (A, aspect 2:3)
```
Edit this ad image. Keep EXACTLY the same layout, all text, colors, fonts, icons, timeline, chat phone mockup, list and bottom button. Change ONLY the man in the top right: replace him with a different man — a Black man in his early 40s with a short trimmed beard, wearing a dark grey hoodie, in a different dark setting (a car interior at night) — same pose holding the phone with both hands looking down at it with a worried, tense expression, same moody neon pink/purple rim lighting. All text must remain exactly as in the original and spelled correctly: "HE DELETED THE EVIDENCE.", "OR AT LEAST HE THOUGHT HE DID.", "2:14 AM Private DM", "2:37 AM Photo sent", "2:41 AM Message deleted", "2:46 AM Photo deleted", "SEE WHAT HE TRIED TO ERASE.", "Private conversations", "Deleted messages", "Deleted photos", "THE DIGITAL FOOTPRINT DOESN'T LIE.", "Tap the button below", "Him", "Active now", "Can't stop thinking about you...", "This message was deleted", "Photo removed", "Message deleted". No logos, no brand names.
```

## 3a-found-hiding-novo-rosto (B, aspect 4:5)
```
Edit this ad image. Keep EXACTLY the same layout, all text, colors, fonts, icons, list, lock box, button and the iPhone with the DM inbox screen. Change ONLY the woman: replace her with a different woman — a white woman in her mid 30s with straight shoulder-length auburn hair, wearing a cream knit sweater — same pose with one hand on her head, the same shocked, distressed expression, holding the same phone toward the camera, same dark room and lighting. All text must remain exactly as in the original and spelled correctly: "Trust but verify...", "I FOUND WHAT HE'S HIDING ON INSTAGRAM.", "Deleted messages", "Hidden chats", "Photos & videos", "Voice messages", "Live location", "Call history", "Contacts", "And more...", "The truth isn't always obvious. But now, it is.", "SEE THE TRUTH NOW", and the chalkboard "Better to know than to guess." Do not add any new logos.
```

## Refações (1 por peça, dentro do teto)

### 1b-he-deleted-dms-v2 (A, 2:3, medium) — v1 trocou o selo flutuante "Message deleted 2:41 AM" para 2:14 AM
```
Edit this ad image. Keep EVERYTHING exactly the same — same man, same pose, same layout, colors, fonts, icons, timeline, chat phone mockup, list and bottom button. Change ONLY the top headline, which must read exactly: "HE DELETED" (white) / "THE DMs." (pink, capital D, capital M, lowercase s), then "OR AT LEAST" (white) / "HE THOUGHT HE DID." (pink). Every other text and number stays exactly as in the original. IMPORTANT: the floating notification next to the man's hand reads exactly "Message deleted" with time "2:41 AM" (not 2:14). Other text, spelled correctly: "2:14 AM Private DM", "2:37 AM Photo sent", "2:41 AM Message deleted", "2:46 AM Photo deleted", "SEE WHAT HE TRIED TO ERASE.", "Private conversations", "Deleted messages", "Deleted photos", "THE DIGITAL FOOTPRINT DOESN'T LIE.", "Tap the button below", chat header "Him" + "Active now", bubble "Can't stop thinking about you..." 2:14 AM, photo 2:37 AM, "This message was deleted" 2:41 AM, "Photo removed" 2:46 AM. No logos, no brand names.
```

### 3a-found-hiding-novo-rosto-v2 (B, 4:5, high) — v1 desenhou logo do Instagram no 1º ícone da lista e errou textos do inbox
```
Edit this ad image. Keep EXACTLY the same layout, all text, colors, fonts, icons, list, lock box, button and the phone screen. Change ONLY the woman: replace her with a different woman — a white woman in her mid 30s with straight shoulder-length auburn hair, wearing a cream knit sweater — same pose with one hand on her head, the same shocked, distressed expression, holding the same phone toward the camera, same dark room and lighting.
Keep the icons in the left list exactly as in the original: the first icon ("Deleted messages") is the same round chat-bubble-with-lightning messenger icon as in the original — do NOT replace it with a camera logo or any other logo. Do not add any new logo anywhere.
All text must remain exactly as in the original and spelled correctly: "Trust but verify...", "I FOUND WHAT HE'S HIDING ON INSTAGRAM.", "Deleted messages", "Hidden chats", "Photos & videos", "Voice messages", "Live location", "Call history", "Contacts", "And more...", "The truth isn't always obvious. But now, it is.", "SEE THE TRUTH NOW", chalkboard "Better to know than to guess."
The phone inbox rows must read exactly, top to bottom (name / preview / time): "chris.off" / "last night was everything" / "01:12"; "blocked" / "save this new one" / "00:58"; "mia.exx" / "I miss u" / "00:42"; "spin.coach" / "after class?" / "00:21"; "private_vault" / "Sent a file" / "Yesterday"; "+1 917 555 0121" / "Voice message" / "Yesterday"; "shh.delete" / "he's asleep now" / "Yesterday"; "lena.k" / "you up?" / "Yesterday". Status bar time "01:24".
```
