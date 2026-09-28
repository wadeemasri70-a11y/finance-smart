# Shot list — Smart Finance Consulting brand clip

Six shots, ~19 s total. Shots 2–4 are the handshake idea from prompt D1,
split up so the labels get their own frames instead of fighting for one.

## Reference frames (in `site/brand/`)

| File | Use |
|------|-----|
| `frame-16x9.png` | 1920×1080 navy frame with the logo. Feed it as the **first frame** of shot 1 and the **last frame** of shot 6, and as the style reference everywhere else. |
| `frame-9x16.png` | 1080×1920, same, for Reels and Stories |
| `logo-transparent.png` | 1600×1300, no background, for overlaying on finished footage |

Video tools want raster, not SVG, which is why these are PNG.

**What a logo reference actually does:** it carries the palette and mood into
the shot. It does **not** make the model redraw your logo correctly. Never
count on the logo appearing in the generated footage — overlay the real one
afterwards.

## Continuity block — append to every prompt

Without this the six shots will not cut together.

```
Consistent look: deep navy background, warm gold accents, a single warm key
light from camera left, soft falloff into deep shadow, shallow depth of field,
85mm lens, subtle film grain, locked-off camera, no camera shake, no text
other than specified.
```

---

## Shot 1 — Logo comes alive · 3 s
Use `frame-16x9.png` as the **first frame** (image-to-video).
```
The three gold bars of the logo slowly extrude upward out of the dark navy
surface while the thin gold ring orbits once around them, volumetric light
catching the gold edges, everything else perfectly still, premium, minimal
```

## Shot 2 — MANDANT · 3 s
```
Extreme close-up of a man's forearm in a dark navy suit sleeve with a crisp
white shirt cuff resting on a dark desk. Large gold embroidered capital
letters on the sleeve clearly read "MANDANT". The text is sharp, in focus,
centred and parallel to the camera. Almost no motion
```

## Shot 3 — SMART FINANCE · 3 s
Same prompt as shot 2, with `"MANDANT"` replaced by `"SMART FINANCE"`, and
the arm entering from the opposite side so the two shots mirror each other.

## Shot 4 — The handshake · 4 s
No text at all in this one; that is why it will actually work.
```
Extreme close-up, two businessmen shaking hands, only forearms and hands in
frame, dark navy suit sleeves, crisp white shirt cuffs, one gold cufflink
catching the light, very slow subtle motion, shot on Arri Alexa
```

## Shot 5 — The work · 3 s
```
Slow push-in over a dark desk, an open laptop showing soft out-of-focus
golden charts, a neat stack of documents, a fountain pen, no people
```

## Shot 6 — End card · 3 s
Use `frame-16x9.png` as the **last frame** so it lands exactly on the logo.
```
Fine golden particles drift slowly through a dark navy void and gather
towards the centre of frame, leaving the middle of the frame clear, elegant,
minimal
```

---

## Edit

1. Order 1 → 6. Cut on motion, not on stillness.
2. Shots 2 and 3 are a matched pair: keep them the same length.
3. Music: something calm, no percussion. Or no music and let the site be quiet.
4. Overlay `logo-transparent.png` on shot 6 — do not rely on the generated logo.
5. Export per `docs/video-option.md`, then send it to me and I will wire it in,
   with scroll scrubbing if you want the same feel the 3D section has now.

## Which shots to expect trouble from

| Shot | Risk |
|------|------|
| 1, 5, 6 | low — no people, no text |
| 4 | medium — hands, but no text |
| 2, 3 | high — text on fabric; generate 4+ takes each and check the spelling letter by letter |

If 2 and 3 never spell correctly, shoot them plain (no lettering) and add the
words in the edit. Nobody will be able to tell.
