# Shot list — Smart Finance Consulting
**6 shots · 24 seconds · 16:9**

No shot contains generated text. All wording is added in the edit, which is
how brand films are made anyway — it is the only way the spelling is
guaranteed and the typeface is your own. Every prompt below is complete and
self-contained: paste it as it stands, nothing to append.

---

## Reference files (`site/brand/`)

| File | Where it is used |
|------|------------------|
| `frame-16x9.png` | first frame of shot 1, last frame of shot 6 |
| `frame-9x16.png` | the vertical cut for Reels and Stories |
| `logo-transparent.png` | the logo overlay on shot 6 |

A logo reference transfers palette and mood only. It will not redraw your logo
correctly, which is why the logo is an overlay, never generated.

## Negative prompt — use on all six shots

```
text, letters, words, numbers, watermark, logo, signature, subtitles,
people's faces, extra fingers, six fingers, deformed hands, merged fingers,
distorted anatomy, blurry, low quality, oversaturated, cartoon, plastic skin,
camera shake, fast motion
```

---

## Shot 1 · Logo materialises · 0:00–0:03

Image-to-video. First frame: `frame-16x9.png`.

```
The three gold bars in the centre of frame slowly extrude upward out of a dark
navy surface while a thin luminous gold ring orbits once around them.
Volumetric light catches the polished gold edges. Deep navy background, warm
gold accents, a single warm key light from camera left, soft falloff into deep
shadow, shallow depth of field, 85mm lens, subtle film grain, locked-off
camera, premium, minimal, 4k.
```

Overlay: none.

---

## Shot 2 · Figures rising · 0:03–0:08

```
Abstract 3D scene, a row of tall polished gold bars of increasing height rising
slowly from a dark navy reflective surface, a thin luminous gold ring drifting
around them, fine golden particles floating in the air, volumetric light beams
from camera left. Deep navy background, warm gold accents, soft falloff into
deep shadow, shallow depth of field, 85mm lens, subtle film grain, very slow
upward camera move, subtle, premium, minimal, 4k.
```

Overlay: none.

---

## Shot 3 · The work · 0:08–0:12

```
Slow cinematic push-in over a dark wooden desk. An open laptop shows soft
out-of-focus golden charts, beside it a neat stack of documents, a fountain
pen and a cup of coffee. Warm golden window light from camera left, deep navy
and gold colour grade, soft falloff into deep shadow, shallow depth of field,
85mm lens, subtle film grain, no people, 4k.
```

Overlay: none.

---

## Shot 4 · The handshake · 0:12–0:17

This is the key shot. Generate at least six takes and pick the one where the
fingers stay intact for the whole clip.

```
Extreme close-up, two businessmen shaking hands, only forearms and hands in
frame. Dark navy suit sleeves, crisp white shirt cuffs, one polished gold
cufflink catching the light. Hands already clasped, holding steady with a very
slow subtle movement. Deep navy background, a single warm key light from
camera left, soft falloff into deep shadow, shallow depth of field, 85mm lens,
subtle film grain, locked-off camera, shot on Arri Alexa, 4k.
```

**Overlay — this is where the two names appear:**

| | Left third | Right third |
|---|---|---|
| Text | SMART FINANCE | MANDANT |
| In | 0:13.0 | 0:13.4 |
| Out | 0:16.6 | 0:16.6 |

Typography for both: Cormorant Garamond SemiBold, 54 px at 1080p, letter-spacing
0.18 em, colour `#CCAA67`, vertically centred, 12 % in from each edge. Fade in
0.4 s, fade out 0.4 s. No box, no shadow — the background is already dark.

---

## Shot 5 · The office · 0:17–0:20

```
Slow dolly through a modern accounting office at golden hour. Empty desks with
monitors, glass partitions, warm sunlight through tall windows, dust motes
drifting in the light beams. Deep navy and gold colour grade, soft falloff into
deep shadow, shallow depth of field, 85mm lens, subtle film grain, no people,
4k.
```

Overlay: none.

---

## Shot 6 · End card · 0:20–0:24

Image-to-video. Last frame: `frame-16x9.png`.

```
Fine golden particles drift slowly through a dark navy void and gather towards
the centre of frame, leaving the centre of the frame clear and empty.
Volumetric light from camera left, soft falloff into deep shadow, shallow depth
of field, subtle film grain, locked-off camera, elegant, minimal, 4k.
```

**Overlay:** `logo-transparent.png` centred, 34 % of frame width, fading in
from 0:21.5 to 0:22.2 and holding to the end.

Optional line under the logo from 0:22.5: *Ihre Zahlen. Ihre Systeme.
Intelligent verbunden.* — Outfit Regular, 26 px, colour `#AFBCC6`,
letter-spacing 0.05 em.

---

## Timeline

```
0:00   0:03        0:08      0:12         0:17     0:20        0:24
 |  1   |     2     |    3    |     4      |   5    |     6     |
                              ^ the two names appear here
                                                    ^ logo overlay
```

## Settings

- 16:9, 1920×1080 or higher, 24 or 25 fps, held consistent across all six.
- Generate each shot 4–6 times and keep the best take.
- Cut on movement, never on a still frame.
- Music: calm, no percussion, fade out under shot 6. Or no music at all.
- Export per `docs/video-option.md`, then send it to me and I will place it in
  the page, with scroll scrubbing if you want the feel the 3D section has now.

## Risk

Every shot except 4 has no people and no text, so it will come out clean on the
first or second try. Shot 4 is the only one that needs patience, because hands
are the weak point of every video model. If six takes do not give you clean
fingers, cut shot 4 shorter — a one second glimpse of the clasp still reads as
a handshake, and the two names carry the meaning anyway.
