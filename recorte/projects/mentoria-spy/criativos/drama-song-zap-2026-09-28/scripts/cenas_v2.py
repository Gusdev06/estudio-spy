# Especificação v2: shot sheets (gpt-image-2/edit) + clipes (minimax-h3 i2v 480p) por bloco.
# Fonte: roteiros/2026-09-28-drama-song-zap/plano-de-cenas.md + personagens.md (DESCRIÇÃO literal).
# Ajustes do Bisturi: blocos com troca de lugar entre quadros viram 2 clipes (pares de quadros do mesmo lugar);
# mãos descritas em positivo; telas de celular só brilho.
import json, pathlib
L = pathlib.Path(__file__).resolve().parent.parent

DESC = {
 "maya-antes": "Maya, a 34-year-old Latina woman with warm light-brown skin, shoulder-length wavy dark-brown hair tied in a messy low bun with loose strands, hazel eyes with faint dark circles, a small beauty mark above the left corner of her upper lip, small gold hoop earrings, wearing an oversized heather-gray cardigan over a plain white t-shirt and dark jeans, slightly hunched posture",
 "maya-depois": "Maya, a 34-year-old Latina woman with warm light-brown skin, shoulder-length wavy dark-brown hair worn down in glossy soft waves, bright hazel eyes, a small beauty mark above the left corner of her upper lip, small gold hoop earrings, subtle burnt-red lipstick, wearing an emerald-green wrap blouse and cream tailored trousers, upright confident posture, chin slightly raised",
 "ryan": "Ryan, a 36-year-old white American man, short dark-blond hair with a neat side part, light stubble, gray-blue eyes, a smug lopsided half-smile, a large silver wristwatch on his left wrist, wearing a navy quarter-zip sweater over a white collared shirt and khaki chinos, athletic build",
 "jess": "Jess, a 33-year-old white woman with fair freckled skin, long wavy copper-auburn hair, green eyes, pearl stud earrings, a wide friendly smile, wearing a blush-pink boat-neck knit sweater and a cream midi skirt",
 "nora": "Nora, a 41-year-old Latina woman with warm light-brown skin, a straight chin-length dark-brown bob with a single silver-gray streak at the front, hazel eyes, calm kind expression, thin gold bangles, wearing a chambray denim shirt with rolled sleeves and reading glasses hooked on the collar, dark trousers",
 "linda": "Linda, a 64-year-old white woman with a short silver bob, rosy cheeks, wearing a floral blouse with a small brooch",
}
NAME = {"maya-antes": "Maya (before)", "maya-depois": "Maya (after)", "ryan": "Ryan", "jess": "Jess", "nora": "Nora", "linda": "Linda"}
KEY = {  # traços marcantes pra lembrar no prompt da imagem
 "maya-antes": "Maya: beauty mark above the left corner of her upper lip, small gold hoops, gray cardigan, messy low bun",
 "maya-depois": "Maya: same face, beauty mark above the left corner of her upper lip, small gold hoops, hair down in soft waves, emerald-green wrap blouse",
 "ryan": "Ryan: lopsided half-smile, large silver watch on his left wrist, navy quarter-zip",
 "jess": "Jess: long copper-auburn hair, freckles, pearl stud earrings, blush-pink sweater",
 "nora": "Nora: chin-length dark bob with one silver-gray streak at the front, chambray shirt, reading glasses on the collar, gold bangles",
 "linda": "Linda: short silver bob, floral blouse, small brooch",
}
SHORT = {  # rótulo curto pro prompt do vídeo
 "maya-antes": "Maya (Latina woman, messy low bun, heather-gray cardigan, small gold hoop earrings, small beauty mark above her lip)",
 "maya-depois": "Maya (Latina woman, dark-brown hair down in soft waves, emerald-green wrap blouse, small gold hoop earrings, small beauty mark above her lip, burnt-red lipstick)",
 "ryan": "Ryan (dark-blond side part, navy quarter-zip, large silver wristwatch, smug half-smile)",
 "jess": "Jess (long wavy copper-auburn hair, freckles, pearl earrings, blush-pink sweater)",
 "nora": "Nora (chin-length dark bob with one silver streak, chambray denim shirt, gold bangles)",
 "linda": "Linda (short silver bob, floral blouse, brooch)",
}
DIN = "a suburban American dining room at night, long wooden table with a white tablecloth, a roast and side dishes, lit candles, warm amber light, dark window in the background"
PHONE = "Any phone screen shows only a soft glow or is dark, never any readable interface, text or logo."

# refs: fichas passadas como imagem (ordem = image 1, 2, ...); bg: descritos só em texto (fundo desfocado)
# clips: lista de (quadro_inicial, quadro_final, fração da duração do bloco, descrição do movimento)
S = {}
S["B01"] = dict(refs=["maya-antes"], bg=["ryan", "jess", "linda"], setting=DIN + ". Maya sits at the table; the other guests are soft and out of focus",
  panels=["frontal close-up of Maya, lost faraway gaze, candle bokeh in the foreground, her hands resting in her lap",
          "rack focus: the blurred background resolves into the guests laughing at the table, Maya soft in the foreground",
          "Maya lowers her eyes to her untouched plate, hands folded on the tablecloth",
          "the camera has pulled back: Maya small and alone in the center of a full, laughing table"],
  # v2: a cantora canta a intro 2x (1,3 s e 9,2 s) -> B01 tem 16,9 s -> 2 clipes
  clips=[(1, 2, 0.5, "Close on Maya's lost, faraway gaze with candle bokeh in the foreground, her hands resting in her lap; the focus slowly shifts to the guests laughing at the table behind her."),
         (3, 4, 0.5, "Maya lowers her eyes to her untouched plate, hands folded on the tablecloth; the camera slowly pulls back until she sits small and alone in the middle of the full, laughing table.")])
S["B02"] = dict(refs=["maya-antes", "ryan", "jess", "linda"], bg=[], setting=DIN + ". Linda at the head of the table, Ryan next to Maya, Jess across the table",
  panels=["high overhead shot of the whole table, dishes being passed from hand to hand",
          "Linda at the head of the table raising her wine glass, smiling",
          "Jess laughing, tossing her copper-auburn hair back",
          "Maya smiling politely, a smile that does not reach her eyes, Ryan beside her"],
  clips=[(1, 4, 1.0, "Starting high above the whole table as dishes pass from hand to hand, the camera cranes down past Linda raising her wine glass and Jess laughing and tossing her hair back, and settles on Maya's polite smile that doesn't reach her eyes, Ryan beside her.")])
S["B03"] = dict(refs=["ryan", "maya-antes"], bg=["linda", "jess"], setting=DIN + ", camera at table height",
  panels=["detail: a phone beside Ryan's plate lights up with a soft glow, his large silver wristwatch next to it",
          "Ryan's hand quickly flips the phone face down",
          "medium shot of Ryan, smug half-smile, glancing sideways at Maya",
          "reverse shot: Maya looking at the face-down phone, brow furrowed, hands in her lap"],
  clips=[(1, 4, 1.0, "Detail of a phone lighting up with a soft glow beside Ryan's plate, his silver watch next to it; his hand quickly flips it face down; he glances sideways at Maya with a smug half-smile; the camera turns to Maya looking at the face-down phone, brow furrowed, her hands resting in her lap.")])
S["B04"] = dict(refs=["maya-antes", "ryan", "linda", "jess"], bg=[], setting=DIN,
  panels=["Maya leans toward Ryan and speaks quietly, lips almost closed",
          "wide shot: everyone at the table stops, forks frozen in the air",
          "close-up of Ryan throwing his head back in a big laugh",
          "Linda and Jess start laughing along, awkward and uncomfortable"],
  clips=[(1, 4, 1.0, "Maya leans toward Ryan and speaks quietly; the whole table freezes, forks in the air; Ryan throws his head back in a big laugh; Linda and Jess start laughing along, awkward.")])
S["B05"] = dict(reuse="shot-sheets/B05.png", refs=["maya-antes", "ryan"], bg=["jess", "linda"],
  clips=[(1, 4, 1.0, "Ryan slides his phone across the white tablecloth until it stops in front of Maya, smug half-smile. Maya's hands stay folded in her lap as she stares at the phone. Ryan turns to the guests with his arms open, laughing. The camera slowly pushes in to a close-up of Maya, eyes glassy with tears, forced polite smile, her hands still folded in her lap, the table laughing blurred behind her.")])
S["B06"] = dict(refs=["maya-antes"], bg=[], setting="a small bathroom in the mother-in-law's house, old green tiles, cold overhead light, a mirror over the sink",
  panels=["Maya closes the door and leans her back against it, eyes closed, palms flat against the door",
          "Maya looks at herself in the mirror and tucks a loose strand of hair behind her ear, practicing a smile",
          "close-up of her reflection in the mirror: the smile fades",
          "Maya has switched off the light; only her dark silhouette remains, a thin line of warm light under the door"],
  clips=[(1, 2, 0.5, "Maya shuts the bathroom door and leans her back against it, eyes closed, palms flat on the door; she steps to the sink and looks into the mirror, tucking a loose strand of hair behind her ear and practicing a smile."),
         (3, 4, 0.5, "Close on Maya's reflection in the mirror as her practiced smile slowly fades; she reaches for the switch and the light goes out, leaving only her dark silhouette and a thin line of warm light under the door.")])
S["B07"] = dict(refs=["maya-antes", "jess"], bg=["ryan"], setting="two bedrooms at 2 a.m.: panels 1 and 4 are Maya's dark bedroom (cold blue window light, Ryan asleep with his back turned, face not visible); panels 2 and 3 are Jess's bedroom lit by a pink bedside lamp",
  panels=["Maya sitting on the edge of the bed, phone held to her ear, cold light from the window, Ryan asleep behind her with his back turned",
          "Jess in her bed, phone held to her ear, worried eyes and a sweet smile, pink lamp light",
          "detail of Jess's nightstand under the pink lamp: a large silver wristwatch identical to Ryan's lying next to the lamp (medium detail shot, not an extreme zoom)",
          "Maya on the bed hugging her knees, phone at her ear, nodding, relieved"],
  clips=[(1, 4, 0.5, "Maya sits on the edge of the bed in the dark, phone held to her ear, cold window light, Ryan asleep behind her with his back turned; she pulls her knees up and hugs them, nodding, relieved."),
         (2, 3, 0.5, "Jess in her bed under a pink lamp, phone held to her ear, worried eyes and a sweet smile; the camera slowly drifts past her to the nightstand, where a large silver wristwatch lies next to the lamp.")])
S["B08"] = dict(refs=["maya-antes"], bg=[], setting="a small counselor's office in late-afternoon light, armchair, bookshelf, a plant. The counselor is a woman in her fifties with gray hair pulled back and a mustard cardigan",
  panels=["Maya in the armchair, leaning forward, distressed, gesturing with open hands",
          "the counselor with her legs crossed, clipboard on her knee, neutral expression",
          "the counselor shrugs with both hands open",
          "Maya sinks back into the armchair, looking at the floor, hands limp in her lap"],
  clips=[(1, 4, 1.0, "Maya leans forward in the armchair, distressed, gesturing with open hands; the counselor with a clipboard on her knee listens with a neutral face and shrugs with both hands open; Maya sinks back into the armchair, staring at the floor, hands limp in her lap.")])
S["B09"] = dict(refs=["maya-antes", "ryan"], bg=[], setting="the couple's bedroom at night, bluish light from the window, a digital clock on the nightstand",
  panels=["top-down view: Maya lying on her back with eyes open, staring at the ceiling, Ryan's side of the bed empty",
          "detail of the digital clock on the nightstand, only a red glow, no readable digits",
          "the door opens: Ryan steps in holding his shoes, his face lit by his phone's glow; Maya pretends to sleep",
          "Maya curled on her side, small in the middle of the big bed"],
  clips=[(1, 4, 1.0, "Top-down on Maya lying awake staring at the ceiling, the other side of the bed empty; a red glow from the bedside clock; the door opens and Ryan tiptoes in holding his shoes, his face lit by his phone's glow, while Maya shuts her eyes and pretends to sleep; she ends curled on her side, small in the middle of the big bed.")])
S["B10"] = dict(refs=["maya-antes", "ryan"], bg=[], setting="Maya's kitchen on a gray rainy morning, rain on the window",
  panels=["Maya in her gray cardigan holding a mug of coffee gone cold with both hands, looking out at the rain",
          "Ryan walks behind her looking at his phone, air-kisses near her head without looking, heading out",
          "the front door has just slammed in the background; the mug trembles in her hands",
          "wide shot: Maya alone in the kitchen, raindrops running down the glass"],
  clips=[(1, 2, 0.5, "Maya holds a cold mug with both hands, gazing at the rain on the window; Ryan walks behind her staring at his phone, air-kisses near her head without looking and heads for the door."),
         (3, 4, 0.5, "The front door slams in the background and the mug trembles in Maya's hands; the camera slowly pulls back to a wide shot of her alone in the kitchen, raindrops running down the glass.")])
S["B11"] = dict(refs=["nora", "maya-antes"], bg=[], setting="the same kitchen at night, warm pendant light, two mugs of tea",
  panels=["the door opens: Nora walks in carrying two mugs of tea, her silver streak lit by the hallway light; Maya at the counter",
          "Nora sets the mugs on the counter and looks at Maya",
          "Maya breaks down; Nora hugs her from the side, firmly",
          "close-up of the two sisters forehead to forehead, Nora's eyes closed"],
  clips=[(1, 4, 1.0, "Nora walks into the warm kitchen carrying two mugs of tea and sets them on the counter, looking at Maya; Maya breaks down and Nora wraps her in a firm side hug; the camera pushes in on the two sisters forehead to forehead, Nora's eyes closed.")])
S["B12"] = dict(refs=["nora", "maya-antes"], bg=[], setting="the same kitchen at night, the sisters at a small kitchen table, warm pendant light",
  panels=["Nora holds both of Maya's hands across the small table",
          "close-up of Nora, calm and steady gaze",
          "Nora pulls her chair closer and pats the seat beside her",
          "Maya hesitates, then sits down next to her sister"],
  clips=[(1, 4, 1.0, "Nora holds both of Maya's hands across the small kitchen table with a calm, steady gaze; she pulls her chair closer and pats the seat beside her; Maya hesitates, then sits down next to her sister.")])
S["B13"] = dict(refs=["nora", "maya-antes"], bg=[], setting="the same kitchen at night, the sisters side by side at the small table, the only light comes from a phone screen",
  panels=["detail: Ryan's phone in a navy-blue case lying on the table between them, screen glowing softly",
          "Nora points at the phone and explains; Maya glances at it sideways",
          "close-up of Maya holding her breath, the screen's glow on her face",
          "close-up of Maya's fingertip touching the glowing screen, the screen out of focus"],
  clips=[(1, 4, 1.0, "A phone in a navy-blue case glows softly on the table between the sisters; Nora points at it and explains while Maya glances sideways; close on Maya holding her breath, the glow on her face; her fingertip reaches out and touches the out-of-focus glowing screen.")])
S["B14"] = dict(refs=["maya-antes", "nora", "jess"], bg=[], setting="panels 1-3: the same dark kitchen, lit only by the phone. Panel 4: a memory of the Sunday dinner, " + DIN,
  panels=["out-of-focus phone screen in the foreground showing only abstract blurred colored shapes, no text; Maya's face sharp behind it",
          "Maya's eyes widen",
          "Maya covers her mouth with her hand; Nora puts a hand on her shoulder",
          "memory insert in warm sepia tone: Jess laughing at the Sunday dinner table, candles"],
  clips=[(1, 3, 0.6, "An out-of-focus glowing phone in the foreground, Maya's face sharp behind it; her eyes slowly widen; she covers her mouth with her hand and Nora rests a hand on her shoulder."),
         (4, None, 0.4, "A warm sepia memory: Jess laughing at the candlelit Sunday dinner table, tossing her copper-auburn hair, slow dreamy push-in.")])
S["B15"] = dict(refs=["maya-antes"], bg=[], setting="the bathroom in Maya's own house, white tiles, mirror over the sink, cold light",
  panels=["close-up of Maya's hands trembling, gripping the edge of the sink",
          "Maya looks at herself in the mirror",
          "her reflection goes slightly blurred and doubled",
          "Maya closes her eyes and takes a deep breath"],
  clips=[(1, 4, 1.0, "Maya's hands tremble as they grip the edge of the sink; she lifts her eyes to the mirror; her reflection goes slightly blurred and doubled; she closes her eyes and takes a deep breath.")])
S["B16"] = dict(refs=["maya-antes"], bg=[], setting="the same bathroom in Maya's house, mirror, cold light, a door to a warm hallway",
  panels=["Maya opens her eyes; her reflection is sharp and clear",
          "she pulls out her hair tie with both hands; her hair falls loose onto her shoulders",
          "she straightens her back, chin up",
          "she has switched off the light and is walking out; the open door lets in warm light from the hallway"],
  clips=[(1, 4, 1.0, "Maya opens her eyes and her reflection is sharp; she pulls out her hair tie with both hands and her hair falls loose onto her shoulders; she straightens her back, chin up; she switches off the light and walks out through the door into warm hallway light.")])
S["B17"] = dict(refs=["maya-depois", "nora"], bg=[], setting="panels 1-2: Maya's bedroom in the morning, sunlight. Panels 3-4: a cozy neighborhood cafe in daylight",
  panels=["Maya sleeping peacefully, morning sun coming in, the gray cardigan tossed on a chair",
          "Maya in a soft white t-shirt opening the curtains, light flooding the room",
          "at the cafe, Nora points at Maya's face and smiles",
          "Maya in the emerald-green wrap blouse laughing for real, hair down"],
  clips=[(1, 2, 0.5, "Maya sleeps peacefully as morning sun comes in, the gray cardigan tossed on a chair; she gets up and pulls the curtains open, sunlight flooding the room."),
         (3, 4, 0.5, "At a sunny cafe table Nora points at Maya's face and smiles; Maya, in her emerald-green blouse with her hair down, laughs for real.")])
S["B18"] = dict(refs=["maya-depois", "ryan", "linda"], bg=[], setting="panels 1-2: Maya's kitchen in daylight. Panels 3-4: the front door of Linda's house",
  panels=["Ryan looks at his phone at the kitchen counter; Maya walks past him serene without looking, in the emerald-green blouse",
          "Ryan, puzzled, watches Maya from behind as she walks away",
          "at the front door of her house, Linda opens the door and sees Maya",
          "Linda tilts her head, curious, and takes Maya's hand in both of hers"],
  clips=[(1, 2, 0.5, "Ryan stares at his phone at the kitchen counter as Maya walks past him, serene, without looking; he looks up, puzzled, and watches her walk away."),
         (3, 4, 0.5, "Linda opens her front door and sees Maya; she tilts her head, curious, and takes Maya's hand warmly in both of hers.")])
S["B19"] = dict(refs=["maya-depois"], bg=[], setting="a suburban street at golden-hour dusk, trees, warm light; a house with a lit window showing a set dinner table",
  panels=["Maya walks toward the camera with a firm stride",
          "lateral tracking shot following her stride, hair swaying",
          "she stops on the sidewalk in front of her mother-in-law's house, the window lit with a set dinner table",
          "close-up: Maya takes a deep breath and smiles with the corner of her mouth"],
  clips=[(1, 2, 0.5, "Maya walks toward the camera down a golden-hour suburban street with a firm stride; the camera tracks alongside her, her hair swaying."),
         (3, 4, 0.5, "Maya stops on the sidewalk in front of a house whose lit window shows a set dinner table; the camera pushes into a close-up as she takes a deep breath and smiles with the corner of her mouth.")])
S["B20"] = dict(refs=["maya-depois", "ryan", "jess", "linda"], bg=[], setting="the same dining room as the first dinner: " + DIN,
  panels=["high overhead shot of the whole table, Maya (after) in the same chair as before",
          "Linda raising her wine glass",
          "Jess laughing, three seats away from Maya",
          "Maya smiling for real, calm"],
  clips=[(1, 4, 1.0, "High overhead shot of the whole candlelit table; the camera cranes down past Linda raising her glass and Jess laughing three seats away, and settles on Maya smiling, calm.")])
S["B21"] = dict(refs=["ryan", "maya-depois", "jess"], bg=["linda"], setting=DIN + ", camera at table height",
  panels=["detail: Ryan's phone lights up with a soft glow beside his plate, his silver watch next to it",
          "Ryan's hand rushes to flip the phone, half a second too late",
          "Maya slowly turns her head to look at Jess",
          "close-up of Jess: her wide smile freezes"],
  clips=[(1, 4, 1.0, "Ryan's phone lights up with a soft glow beside his plate; his hand rushes to flip it, a beat too late; Maya slowly turns her head to look down the table at Jess; close on Jess as her wide smile freezes.")])
S["B22"] = dict(refs=["maya-depois", "ryan", "jess", "linda"], bg=[], setting=DIN,
  panels=["medium two-shot, mirror of the first dinner: Maya calmly slides Ryan's face-down phone back across the tablecloth to him, smiling",
          "close-up of Ryan: his half-smile drops",
          "wide shot: everyone at the table frozen, forks in the air",
          "Maya stands up calmly, handbag on her shoulder, walking out of frame; the candles flicker"],
  clips=[(1, 4, 1.0, "Maya calmly slides Ryan's face-down phone back across the tablecloth to him, smiling; his half-smile drops; the whole table freezes, forks in the air; Maya stands up, puts her handbag on her shoulder and walks out of frame as the candles flicker.")])
S["B23"] = dict(refs=["maya-depois"], bg=[], setting="the front porch of Maya's house at night, warm porch light, Maya sitting on the step",
  panels=["medium shot: Maya sitting on the porch step, looking out at the street, hands clasped around her knees",
          "she turns her head and looks straight into the camera",
          "frontal close-up, steady and warm gaze",
          "a slight knowing nod"],
  clips=[(1, 4, 1.0, "Maya sits on the porch step at night, hands clasped around her knees, looking at the street; she turns and looks straight into the camera; the camera pushes into a warm, steady close-up and she gives a slight knowing nod.")])
S["B24"] = dict(refs=["maya-depois"], bg=[], setting="the same front porch at night, warm porch light",
  panels=["Maya holds her own phone turned toward her body; only its glow shows",
          "close-up of the screen's glow on her calm face",
          "she rests the phone face down on her knee and looks at the camera",
          "she smiles and settles back, relaxed"],
  clips=[(1, 4, 1.0, "Maya holds her phone turned toward herself, only its glow lighting her calm face; she lays the phone face down on her knee and looks into the camera; she smiles and settles back, relaxed.")])
S["B25"] = dict(refs=["maya-depois"], bg=[], setting="the same front porch at night, warm porch light, the front door behind her",
  panels=["Maya points down toward the bottom of the frame with one finger, smiling",
          "close-up of her smiling",
          "she stands and walks into the house; the doorway light outlines her",
          "the front door left ajar, warm light spilling out onto the empty porch"],
  clips=[(1, 4, 1.0, "Maya smiles and points down toward the bottom of the frame; she stands up and walks into the house, outlined by the warm doorway light; the front door is left ajar, warm light spilling onto the empty porch.")])

HEAD = ("A 2x2 grid storyboard in a single image, four sequential moments of the same continuous shot, read left-to-right, "
        "top-to-bottom. Thin white gutters between panels. No text, no captions, no panel numbers.")
TAIL = ("3D animated feature film style, cinematic lighting, shallow depth of field, consistent characters, outfits and lighting "
        "across panels, vertical 9:16 framing inside each panel.")

def sheet_prompt(k, s):
    refs = s["refs"]
    intro = " ".join(f"Image {i+1} is the character sheet for {NAME[r]}." for i, r in enumerate(refs))
    keep = ("Keep their faces, hair, outfits and signature details exactly as in the sheets (" + "; ".join(KEY[r] for r in refs) + ").")
    chars = " ".join(DESC[r] + "." for r in refs)
    if s["bg"]: chars += " In the background, soft and out of focus: " + " ".join(DESC[r] + "." for r in s["bg"])
    pan = "\n".join(f"Panel {i+1}: {p}." for i, p in enumerate(s["panels"]))
    return f"{intro} {keep}\n{HEAD}\nSetting (same in all four panels unless stated): {s['setting']}.\nCharacters: {chars}\n{pan}\n{PHONE}\n{TAIL}"

def clip_prompt(k, s, desc):
    who = [SHORT[r] for r in s["refs"]]
    return ("One continuous vertical shot, 3D animated feature film style. " + desc + " Characters: " + "; ".join(who) + ". "
            "Same faces, hair and outfits throughout, cinematic lighting, shallow depth of field, slow smooth camera. "
            "Any phone screen stays black or shows only a soft blank glow, never icons, apps or text. "
            "No text, no subtitles, no phone interface. Soft room ambience only, no speech, no music.")

if __name__ == "__main__":
    urls = {r: json.load(open(L / f"_runs/ficha-{r}.out.json"))["outputs"][0] for r in DESC}
    for k, s in S.items():
        if s.get("reuse"): continue
        inp = {"prompt": sheet_prompt(k, s), "images": [urls[r] for r in s["refs"]], "aspect_ratio": "9:16",
               "resolution": "1k", "quality": "high", "output_format": "png"}
        json.dump(inp, open(L / f"_runs/shot-v2-{k}.json", "w"), indent=1, ensure_ascii=False)
    print("ok", len(S))
