# Shot list — Smart Finance Consulting
**5 shots · 15 seconds · 16:9 · text-to-video**

Pure text-to-video: no image input anywhere. Every prompt is complete and
self-contained — paste it as it stands and nothing needs to be appended.

No shot contains generated text. All wording, and the logo itself, are added in
the edit. That is how brand films are made anyway, and with no reference image
in play it is the only way your mark appears correctly at all.

## The look sentence

Without an image reference, consistency across the five shots comes from one
thing only: this sentence appearing **word for word** at the end of every
prompt. It is already included in each prompt below. Do not paraphrase it, and
do not change the wording between shots, or they will not cut together.

```
Deep navy background, warm gold accents, a single warm key light from camera
left, soft falloff into deep shadow, shallow depth of field, 85mm lens, subtle
film grain, locked-off camera, 4k.
```

If your tool exposes a seed, reuse the same seed across all five shots.

## Negative prompt — use on all five shots

```
text, letters, words, numbers, watermark, logo, signature, subtitles,
people's faces, extra fingers, six fingers, deformed hands, merged fingers,
distorted anatomy, blurry, low quality, oversaturated, cartoon, plastic skin,
camera shake, fast motion
```

Generate each shot at whatever length your tool produces (most give 5–10 s) and
trim to the durations below, taking the calmest stretch rather than the start.

---

## Shot 1 · The mark forms · 0:00–0:02.5 · 2.5 s

```
Abstract 3D animation. Three polished gold bars of increasing height rise
slowly out of a dark navy reflective surface in the centre of frame, and a
thin luminous gold ring sweeps once around them in a tilted orbit. Volumetric
light catches the polished gold edges. Nothing else in frame, generous empty
space around the shapes. Deep navy background, warm gold accents, a single warm
key light from camera left, soft falloff into deep shadow, shallow depth of
field, 85mm lens, subtle film grain, locked-off camera, 4k.
```

Overlay: none.

---

## Shot 2 · Figures rising · 0:02.5–0:05.5 · 3 s

```
Abstract 3D scene, a row of tall polished gold bars of increasing height rising
slowly from a dark navy reflective surface, a thin luminous gold ring drifting
around them, fine golden particles floating in the air, volumetric light beams
from camera left, very slow upward camera move. Deep navy background, warm gold
accents, a single warm key light from camera left, soft falloff into deep
shadow, shallow depth of field, 85mm lens, subtle film grain, locked-off
camera, 4k.
```

Overlay: none.

---

## Shot 3 · The work · 0:05.5–0:08 · 2.5 s

```
Slow cinematic push-in over a dark wooden desk. An open laptop shows soft
out-of-focus golden charts, beside it a neat stack of documents, a fountain pen
and a cup of coffee. No people in frame. Deep navy background, warm gold
accents, a single warm key light from camera left, soft falloff into deep
shadow, shallow depth of field, 85mm lens, subtle film grain, locked-off
camera, 4k.
```

Overlay: none.

---

## Shot 4 · The handshake · 0:08–0:12 · 4 s

The key shot. Generate at least six takes and keep the one where the fingers
stay intact for the whole clip.

```
Extreme close-up, two businessmen shaking hands, only forearms and hands in
frame, no faces. Dark navy suit sleeves, crisp white shirt cuffs, one polished
gold cufflink catching the light. The hands are already clasped and hold steady
with a very slow subtle movement. Deep navy background, warm gold accents, a
single warm key light from camera left, soft falloff into deep shadow, shallow
depth of field, 85mm lens, subtle film grain, locked-off camera, 4k.
```

**Overlay — the two names appear here:**

| | Left third | Right third |
|---|---|---|
| Text | SMART FINANCE | MANDANT |
| Fade in | 0:08.8 | 0:09.2 |
| Fade out | 0:11.7 | 0:11.7 |
| On screen | 2.9 s | 2.5 s |

Typography for both: Cormorant Garamond SemiBold, 54 px at 1080p,
letter-spacing 0.18 em, colour `#CCAA67`, vertically centred, 12 % in from each
edge. Fade in 0.4 s, fade out 0.4 s. No box, no shadow — the plate is already
dark.

---

## Shot 5 · End card · 0:12–0:15 · 3 s

```
Fine golden particles drift slowly through a dark navy void and gather into a
soft glowing cluster, leaving the very centre of the frame clear and empty.
Volumetric light from camera left. Deep navy background, warm gold accents, a
single warm key light from camera left, soft falloff into deep shadow, shallow
depth of field, 85mm lens, subtle film grain, locked-off camera, 4k.
```

**Overlay:** `site/brand/logo-transparent.png` centred, 34 % of frame width,
fading in from 0:12.8 to 0:13.4 and holding to the end. This is the only place
your logo appears, so do not skip it.

No tagline at this length — it would be on screen for barely a second.

---

## Timeline

```
0:00      0:02.5        0:05.5     0:08              0:12        0:15
 |   1     |      2      |    3     |        4        |     5     |
                                      ^ names 0:08.8   ^ logo 0:12.8
```

## Settings

- 16:9, 1920×1080 or higher, 24 or 25 fps, the same figure on all five shots.
- Generate each shot 4–6 times and keep the best take.
- Cut on movement, never on a still frame.
- Music: calm, no percussion, fading out under shot 5. Or none at all.
- Export per `docs/video-option.md`, then send it to me and I will place it in
  the page, with scroll scrubbing if you want the feel the 3D section has now.

## Risk

Four of the five shots have no people and no text, so they come out clean on
the first or second try. Shot 4 is the only one needing patience, because hands
are the weak point of every video model. If six takes do not give clean
fingers, cut shot 4 to 3 seconds and give shot 2 the extra second — a short
glimpse of the clasp still reads as a handshake, and the two names carry the
meaning regardless.

## Vertical cut (9:16, for Reels)

Same five shots, same order and the same prompts — just switch the tool to
9:16 rather than cropping, because cropping a 16:9 close-up cuts the hands in
half. In shot 4 stack the two names as centred lines instead of left and right.

## Optional swap — office instead of desk

Replace shot 3 with this, same 2.5 s:

```
Slow dolly through a modern accounting office at golden hour. Empty desks with
monitors, glass partitions, warm sunlight through tall windows, dust motes
drifting in the light beams, no people in frame. Deep navy background, warm
gold accents, a single warm key light from camera left, soft falloff into deep
shadow, shallow depth of field, 85mm lens, subtle film grain, locked-off
camera, 4k.
```
