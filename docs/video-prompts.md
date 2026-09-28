# Video prompts — Smart Finance Consulting

## Read this first: never ask the AI for the name or the logo

Video models cannot spell. Ask for "Smart Finance Consulting" in the shot and
you get warped pseudo-letters — "SMRAT FNANCE", drifting and morphing between
frames. The same goes for the logo: it will come back as a smear that looks
like your mark but is not it.

So: **generate a clean plate with no text, then add the name and logo on top.**
You already have `site/logo-smart-finance.svg`, which is sharp at any size.
The overlay can be done in the video editor, or on the website in CSS over the
video — ask me and I will wire it up, it costs nothing and stays pixel-perfect.

Every prompt below therefore describes an empty, brand-coloured shot with room
left for the logo.

---

## A. Brand colours, no people — highest success rate

**A1 — golden bars rising (your logo, as a scene)**
```
Abstract 3D animation, three tall polished gold bars of increasing height rising
slowly from a dark navy surface, a thin luminous golden ring orbiting around them,
volumetric light, deep navy background, shallow depth of field, slow upward camera
move, cinematic, premium, minimal, 4k
```
Leave headroom in the frame; the wordmark goes underneath.

**A2 — light across a desk**
```
Slow cinematic push-in over a dark wooden desk, an open laptop showing soft
out-of-focus charts, a few stacked papers, a fountain pen, a cup of coffee, warm
golden window light from the left, deep navy and gold colour grade, shallow depth
of field, no people, no text, 35mm, shot on Arri Alexa
```

**A3 — paper becoming data**
```
Cinematic macro shot, a sheet of paper dissolving into small glowing golden
particles that drift upward and reassemble into a clean grid, dark navy
background, volumetric light, slow motion, elegant, minimal, no text
```

---

## B. The handshake — only if you insist

Hands are the weakest point of every video model: extra fingers, fingers melting
together, the grip sliding apart. Budget many attempts, and cut away from the
grip quickly.

**B1**
```
Extreme close-up, two businessmen in dark navy suits with crisp white shirt cuffs
shaking hands, only forearms and hands in frame, warm golden key light from the
left, dark navy background, shallow depth of field, very slow subtle motion,
cinematic, 85mm, shot on Arri Alexa
```

**B2 — safer, avoids the grip**
```
Close-up of two hands passing a folder of documents across a desk, dark navy suit
sleeves, white cuffs, warm office light, dark navy and gold tones, slow dolly in,
shallow depth of field, cinematic, no faces, no text
```

**Negative prompt** (paste wherever the tool allows one)
```
text, letters, words, watermark, logo, signature, extra fingers, six fingers,
deformed hands, merged fingers, distorted anatomy, warped limbs, blurry, low
quality, oversaturated, cartoon, plastic skin
```

---

## C. Office in Neuss

**C1**
```
Slow cinematic dolly through a modern accounting office at golden hour, empty
desks with monitors, glass partitions, warm sunlight through large windows, dust
motes in the light beams, deep navy and gold colour grade, no people, no text, 4k
```

---

## Settings

- 3–6 seconds. Short clips hold together; long ones drift.
- 16:9 for the section, and shoot a 9:16 version too if you want it for Reels.
- Locked-off or very slow camera. Fast moves make the artefacts obvious.
- Generate at least 4 takes per prompt and keep the best.
- If the tool takes an image input, feed it a still from your brand — it holds
  the colours far better than words alone.

## Before you publish

- Check the tool's licence covers **commercial use**; several free tiers do not.
- Keep the receipt and licence text.
- If the clip is AI-generated and shows people, do not present them as your team
  or your clients.

---

# D. With the German labels in shot

Requested: the sleeves carry "SMART FINANCE" and "MANDANT". Note that
**Mandant** is the correct German word for the client of a tax or accounting
firm — *Kunde* is what a shop has, and reads wrong on a Steuerberatung site.

Whether a model can spell these depends entirely on which model you use.
Veo 3, Sora 2 and Kling 2.5 manage short uppercase words fairly often; older
and cheaper models essentially never do. Two rules decide the outcome:

1. **Fewer characters win.** One word beats two. "MANDANT" (7) is realistic,
   "SMART FINANCE" (12) is borderline, "SMART FINANCE CONSULTING" will fail.
2. **Flat and still beats curved and moving.** Text wrapped around a moving
   sleeve is the hardest case there is. On a flat, static surface — a card, a
   nameplate, a folder — the same model succeeds far more often.

Try these in order and stop at the first that works.

### D1 — one label per shot, then cut between them (best odds)

Shot 1:
```
Extreme close-up of a man's forearm in a dark navy suit sleeve with a crisp
white shirt cuff, resting on a dark desk. Large gold embroidered capital
letters on the navy sleeve clearly read "MANDANT". The text is sharp, in
focus, centred and parallel to the camera. Warm golden light from the left,
dark navy background, shallow depth of field, almost no motion, cinematic, 85mm
```

Shot 2: the same prompt with `"MANDANT"` replaced by `"SMART FINANCE"`.

Then cut to a handshake shot with no text at all (prompt B1).

### D2 — both labels, one shot (what you asked for)

```
Extreme close-up, two businessmen shaking hands, only forearms in frame, dark
navy suit sleeves and crisp white shirt cuffs. The left sleeve has large gold
embroidered capital letters clearly reading "SMART FINANCE". The right sleeve
has large gold embroidered capital letters clearly reading "MANDANT". Both
words are sharp, in focus and parallel to the camera. Warm golden key light
from the left, dark navy background, shallow depth of field, very slow motion,
cinematic, 85mm, shot on Arri Alexa
```

### D3 — text on flat objects instead of sleeves (most reliable of the three)

```
Cinematic close-up of two business cards lying side by side on a dark navy
desk. The left card reads "SMART FINANCE" in gold capital letters, the right
card reads "MANDANT" in gold capital letters. A hand enters and slides the two
cards together until they touch. Warm golden light from the left, shallow
depth of field, slow motion, no other text, 4k
```

### Negative prompt for all of D

```
misspelled text, gibberish text, distorted letters, duplicated letters, extra
words, watermark, extra fingers, deformed hands, merged fingers, blurry text,
low quality
```

### If the spelling still comes out wrong

Generate the clip **without** any text and add the words afterwards. The
current 3D section already does exactly this — the labels are drawn as real
text on the sleeves, so they are always correctly spelled at any resolution.
The same overlay works over a video; send me the clip and I will place them.
