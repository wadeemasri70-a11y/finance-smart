# Shot list — Smart Finance Consulting
**4 shots · 15 seconds · 16:9 · with logo reference**

Each prompt below is one complete block: subject, action, camera, lens,
lighting, colour, texture, mood and quality are all inside it. Paste one block
per shot. Nothing to append, nothing to remember.

No shot contains generated text. The two names and the logo are added in the
edit — with a reference image in play the model will still not spell or redraw
your mark correctly, and overlays are exact at any resolution.

## Reference image

Use `site/brand/frame-16x9.png` on all four shots, attached differently
depending on the shot:

| Shot | How to attach it |
|------|------------------|
| 1 | as the **first frame** (image-to-video) |
| 2 | as a **style reference** (palette only) |
| 3 | as a **style reference** (palette only) |
| 4 | as the **last frame** |

For Reels use `frame-9x16.png` the same way.

## Negative prompt — all four shots

```
text, letters, words, numbers, watermark, logo, signature, subtitles, faces,
extra fingers, six fingers, deformed hands, merged fingers, distorted anatomy,
blurry, low quality, oversaturated, cartoon, plastic skin, camera shake,
fast motion, jump cut
```

Generate each shot at whatever length the tool gives (usually 5–10 s) and trim
to the durations below, taking the calmest stretch rather than the opening
frames. Same fps on all four — 24 or 25.

---

## Shot 1 · The mark comes alive · 0:00–0:03 · 3 s
First frame: `frame-16x9.png`

```
Cinematic abstract 3D animation, matching the colour palette and mood of the
reference image. Three polished gold bars of increasing height stand in the
centre of a dark navy reflective floor and rise slowly upward, while a thin
luminous gold ring sweeps once around them in a tilted elliptical orbit. Warm
volumetric light beams enter from camera left and catch the polished edges of
the gold; the reflections travel slowly along each bar. Fine dust particles
drift through the light. The frame stays generously empty around the shapes.
Deep navy background, warm gold accents, single warm key light from camera
left, soft falloff into deep shadow, shallow depth of field, 85mm lens, very
slow push in, locked-off tripod, subtle film grain, premium, minimal,
photorealistic render, 4k.
```

Overlay: none.

---

## Shot 2 · The work · 0:03–0:06.5 · 3.5 s
Style reference: `frame-16x9.png`

```
Slow cinematic push-in across a dark walnut desk in a quiet office, matching
the colour palette and mood of the reference image. An open laptop sits
slightly left of centre showing soft out-of-focus golden charts, beside it a
neat stack of white documents, a black fountain pen resting on top, and a cup
of coffee with a thin wisp of steam. Warm golden late-afternoon light rakes in
from camera left across the desk surface, picking out the grain of the wood and
the edges of the paper. No people anywhere in frame. Deep navy background, warm
gold accents, single warm key light from camera left, soft falloff into deep
shadow, very shallow depth of field, 85mm lens, slow dolly in, locked-off
tripod, subtle film grain, calm, premium, photorealistic, 4k.
```

Overlay: none.

---

## Shot 3 · The handshake · 0:06.5–0:11.5 · 5 s
Style reference: `frame-16x9.png`

The key shot, and the only demanding one. Generate at least six takes and keep
the one where the fingers stay intact through the whole clip.

```
Extreme close-up of a business handshake, matching the colour palette and mood
of the reference image. Only the two forearms and the clasped hands are in
frame, no faces and no bodies. Both men wear dark navy suit sleeves over crisp
white shirt cuffs, and one polished gold cufflink catches a highlight. The
hands are already firmly clasped when the shot begins and hold steady, with
only a very slow settling movement and the faintest shift of the fingers. Warm
golden key light from camera left rims the knuckles and the white cuffs against
the darkness behind. Deep navy background, warm gold accents, single warm key
light from camera left, soft falloff into deep shadow, shallow depth of field
with the grip in sharp focus, 85mm lens, locked-off tripod, no camera movement,
subtle film grain, shot on Arri Alexa, photorealistic, 4k.
```

**Overlay — the two names appear here:**

| | Left third | Right third |
|---|---|---|
| Text | SMART FINANCE | MANDANT |
| Fade in | 0:07.3 | 0:07.7 |
| Fade out | 0:11.2 | 0:11.2 |
| On screen | 3.9 s | 3.5 s |

Typography for both: Cormorant Garamond SemiBold, 54 px at 1080p,
letter-spacing 0.18 em, colour `#CCAA67`, vertically centred, 12 % in from each
edge. Fade in 0.4 s, fade out 0.4 s. No box and no drop shadow — the plate
behind is already dark.

---

## Shot 4 · End card · 0:11.5–0:15 · 3.5 s
Last frame: `frame-16x9.png`

```
Cinematic abstract shot, matching the colour palette and mood of the reference
image. Fine golden particles drift slowly upward through a dark navy void and
gather into a soft glowing cluster, while the very centre of the frame stays
clear and empty. A faint warm glow builds behind the particles as they settle.
Warm volumetric light from camera left. Deep navy background, warm gold
accents, single warm key light from camera left, soft falloff into deep shadow,
shallow depth of field, 85mm lens, locked-off tripod, almost no motion, subtle
film grain, elegant, minimal, photorealistic, 4k.
```

**Overlay:** `site/brand/logo-transparent.png` centred, 34 % of frame width,
fading in from 0:12.3 to 0:12.9 and holding to the end. This is the only place
your logo appears in the film, so do not skip it.

No tagline at this length — it would be readable for barely a second.

---

## Timeline

```
0:00        0:03           0:06.5                  0:11.5           0:15
 |     1     |       2      |           3           |        4       |
                              ^ names in 0:07.3       ^ logo in 0:12.3
```

## Edit

1. Order 1 → 4, cut on movement rather than on a still frame.
2. Music calm and without percussion, fading out under shot 4. Or none at all.
3. Export per `docs/video-option.md`, then send me the file and I will place it
   in the page, with scroll scrubbing if you want the feel the 3D section has.

## Risk

Shots 1, 2 and 4 have no people and no text and will come out clean on the
first or second try. Shot 3 is the only one that needs patience, because hands
are the weak point of every video model. If six takes do not give clean
fingers, trim shot 3 to 3.5 s and give shot 1 the extra time — a brief glimpse
of the clasp still reads as a handshake, and the two names carry the meaning.

## Vertical cut (9:16)

Same four shots and the same prompts; switch the tool's aspect ratio rather
than cropping, because cropping a 16:9 close-up cuts the hands in half. In
shot 3 stack the two names as centred lines instead of left and right.
