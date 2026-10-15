---
tipo: fonte-crua
data_coleta: 2026-09-28
fonte: https://maxfusion.ai/blog/how-to-make-a-drama-style-song-vsl
autor: Ori Silver (co-founder, Maxfusion AI) — publicado 2026-09-25
metodo: curl do HTML + extração de texto (rodapé de navegação removido). Texto verbatim do artigo.
avisos:
  - É artigo de FORMATO de um vendedor de ferramenta (Maxfusion), com CTA pro próprio MCP. Não é anúncio da Ad Library.
  - "eleven to fourteen million dollars a month" da Resilia é ESTIMATIVA do autor, sem fonte. Não verificado.
  - O vídeo de exemplo ("LC by Maxfusion") é um player embutido (Framer) sem URL de arquivo exposta no HTML; só o canal https://www.youtube.com/@maxfusion-ai aparece como link.
imagens_do_artigo:
  - "The hero's journey inside a Resilia song ad": https://framerusercontent.com/images/5SJMXpgvQ0ozVH0t9Km0hJB310o.webp
  - "A page of the LC Lymphatic Complex song VSL script": https://framerusercontent.com/images/uXiCAHIhVpGZ7hoiN2bUuXl1f7Q.webp
  - "A section of the LC timing map": https://framerusercontent.com/images/scvEOM2YUYuH5XElXHcd2MXV4.webp
  - "LC character sheet: the narrator": https://framerusercontent.com/images/y9PUcYZXntRX76Uc4TYHDFSuDQ.webp
  - "LC character sheet: the narrator after her transformation": https://framerusercontent.com/images/aI9liiaJfWNeWdcJ9elzzhiZUi0.webp
  - "An LC shot sheet with four frames": https://framerusercontent.com/images/XTyay6ao24BnRnu2s253ytbJoiA.webp
---

# How to Make a Drama-Style Song VSL With AI: The Full Process

Ori Silver

·

Co-founder, Maxfusion AI

·

September 25, 2026

You’ve probably seen Resilia’s drama-style song VSLs. Resilia sells an oregano oil and black seed oil softgel, and it makes an estimated eleven to fourteen million dollars a month, much of it from this exact format: a five-to-ten-minute mini drama, delivered as a song, that speaks directly to the sub-avatar.
I analyzed their top-performing ads and took apart the blueprint behind them.
This guide shows you how to make the same kind of drama-style song VSL, step by step, from the script to the finished edit. It covers both routes: doing it through the Maxfusion AI MCP, and doing it by hand.

The finished ad first

PLAY

The ad above is for LC by Maxfusion, a lymphatic support complex. It was made with the exact process in this article.

The process at a glance
1. Script: write the drama on the hero’s journey.
2. Song: turn the script into a song, word for word.
3. Timing map: find the exact second every word is sung.
4. Character sheets: build a reference sheet for every character.
5. Shot sheets: draw every shot as a grid of four frames.
6. Videos: turn each shot sheet into a clip.
7. Edit: stitch the clips in order and lay the song underneath.
Every stage after the script and the song is built to match them, so get those two right before you touch a single image.
Choose a genre and a pace that let every word be heard clearly and never cut a line in an important place.
I worked through the Maxfusion MCP, so Claude created a new project for the ad at the start, and every image and every video was saved there, organized in one place.

Stage 1: the script
The script is the backbone of the entire ad. In any format, a good script carries most of the weight of a successful ad, and in a VSL like this it carries almost all of it, because the story is the ad. If the story is weak, the visuals mean very little.
Start with the product and the sub-avatar: what the product does, who the ad is for, and the fear that person keeps to themselves. The sub-avatar decides every character and every scene.
The story follows a very specific hero’s journey, drawn as a fall and a rise.

Brainstorm a few story arcs with Claude before you commit to one, then flesh out the one you pick. For each arc, pin down the hook line, the betrayer, the mentor, the truth the mentor reveals, and the vindication scene. Example: a wife whose husband cropped her out of the family photo, a college roommate who is now a lymphatic therapist, and a graduation where he asks the photographer for a photo of just her.
The overview of the story. The first half is pain. The hero is humiliated and it gets worse, then they freeze, see that the insult is true, and hit rock bottom after every fix fails, including the advice of friends and the usual authority figures. Around the halfway point a close, credible mentor reveals the truth and hands over the product. The second half is the climb: doubt, then week-by-week changes other people notice, then vindication in the same place as the humiliation. The last minute or so is the pitch to the viewer.
Write the script as lyrics, in the first person, with short lines and one idea per line. Seven to ten minutes of song is roughly 1,100 to 1,500 words.

Stage 2: the song
Once the script is done, there are two ways to turn it into a song.
I used the Maxfusion MCP, which has access to all the latest music models, so Claude sent the lyrics straight from the chat, at the same quality you’d get anywhere else.
If you have a Suno account, you can do it yourself: log in, paste the lyrics, pick a style, and generate.
Either way, give the model the script as the lyrics and ask for it to be sung exactly as written. Pick a voice that matches the narrator. Example: slow R&B with a female vocalist in her forties.
A drama-style VSL is long, and Suno caps the lyrics at 5,000 characters, so the whole song won’t fit in one generation and you’ll need two. Keep the style prompt exactly the same in both. End the first part on a chorus in the middle of the story and let it ring out with no outro, so it can crossfade into the second part, which starts right on the vocal with no intro.
Part one:
Style: Slow-burn contemporary R&B, 110 BPM, in A minor, female vocalist in her 40s, warm and soulful, half-sung verses with intimate spoken lines, soft keys and rim-click groove, strips down in the verses, full lift on the choruses and the results verse, spoken outro over the beat. End on the chorus, let it ring out.
Part two:
Style: Slow-burn contemporary R&B, 110 BPM, in A minor, female vocalist in her 40s, warm and soulful, half-sung verses with intimate spoken lines, soft keys and rim-click groove, strips down in the verses, full lift on the choruses and the results verse, spoken outro over the beat. Start directly on the vocal, no intro.
Then have Claude crossfade and stitch the two parts together locally, and you have the full song. If you made the parts in Suno yourself, you can also join them by hand in CapCut.

Stage 3: the timing map
The timing map lists every line of the song with the second it starts and the second it ends.
To build it, have Claude run the song through Whisper locally with word timestamps. Take the timestamps from Whisper and the words from your script, because Whisper mishears sung lyrics.
The video model can only make clips of limited length, so the song gets cut into chunks. The timing map tells you exactly which lines each chunk covers and how long it has to be.

Stage 4: character sheets
List every character in the script and make a character sheet for each one. A character sheet shows the same character four times on a plain background: a close-up of the face, a full body front view, and two three-quarter views.

When a character changes during the story, make another sheet. Example: the narrator before and after her transformation.

Smaller changes, like a new outfit in one scene, can go straight into the prompt while you keep using the same sheet.
Use 3D animation in the look of an animated feature film unless you want something else, like claymation or a realistic look. Describe the look in the prompt and keep that description identical in every image and video prompt.
Generate the images with GPT Image 2, which holds characters consistent. Nano Banana Pro also works if you want to save credits. Weaker image models make the whole ad look cheap.

Stage 5: shot sheets
Build the shots as shot sheets instead of single images. A shot sheet is one image split into a grid of four frames, and each frame is a moment of the same shot.

Plan the shots from the timing map, so each sheet covers the lines sung in its chunk of the song. In the prompt, describe the setting once, then each of the four frames: where the camera is and the one action happening in it. Attach the character sheets for everyone in the shot, and the product image when the product appears.
Generate one sheet first and check it before you make the rest.

Stage 6: the videos
Turn each shot sheet into a video clip with Seedance 2.0. Attach the shot sheet and the character sheets as references. In the prompt, tell the model the shot sheet is a storyboard to follow and that it must never appear in the video, then give the timing of each frame inside the clip. Say it again as the last line of the prompt.
Seedance 2.0 is cheaper than Seedance 2.5 and still gets the work done. Its reasoning is strong enough to read a shot sheet and turn it into well-directed shots. There is a small risk that the grid itself shows up in the video, but with Seedance 2.0 this rarely happens.
Cheaper, weaker video models end up costing more. They produce so many bad clips that one ad can take hundreds of generations.
Set the length of each clip from the timing map, never from a fixed number. Every clip has to match the words it covers, so one might be eight seconds and the next fourteen.
Keep the clips silent. The song goes on in the edit.
Generate the first one or two clips on their own and check them before you send the rest in small batches. It’s tempting to send everything at once, but small batches catch a problem before it repeats across the whole ad.

Stage 7: the edit
You can edit the clips yourself from the Maxfusion project, or have Claude do it locally with ffmpeg.
Claude cuts each clip to its exact slot in the timing map, puts them in order, and lays the song underneath as the only audio. Check the start of every clip, because a clip can open on a flash of the shot sheet or a still frame, and trim those frames off.
Don’t wait for the last clip to start editing. Once the first few minutes of clips are ready, stitch that section and watch it. Fixes are cheaper while the rest is still being made.
Add captions at the end with Max Captions.
