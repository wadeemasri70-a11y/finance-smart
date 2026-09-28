# Video instead of the 3D handshake

## What I can and cannot do here

I have no video generation model available in this session (no Sora, Veo,
Runway or Kling tool), and no ffmpeg to transcode one. So you generate or
buy the clip, send me the file, and I wire it into the page.

## Before you spend money on AI video

Hands are the single worst subject for AI video. Extra fingers, fingers
merging into each other, and grips that slide apart are the classic failure
mode, and a handshake close-up is the hardest version of it. Expect to throw
away a lot of generations. Use AI video for atmosphere instead — documents
moving, numbers, an office at dusk — and not for the handshake itself.

## Options, best first

| Option | Cost | Reliability | Trust value |
|--------|------|-------------|-------------|
| **Film it yourself** — owner and office in Neuss, phone on a tripod, window light | ~0 | high | **highest** — a real face beats any CGI for a Steuerberatung |
| **Licensed stock clip** — Coverr (free), Pexels, Pixabay, Artgrid | 0–50 € | high | medium |
| **AI video** | 10–100 € in retries | low for hands | low, and it can read as fake |
| **Keep the 3D** (current) | done | — | medium, and it is the only one that reacts to scrolling |

## The option worth considering: scroll-scrubbed video

A normal video just plays. The 3D handshake currently follows the scroll —
the visitor drives it. You can have both: take a real clip and seek it by
scroll position, which is the technique Apple uses on its product pages.
Same feel as now, but with real footage.

Requirements: short (3–6 s), locked-off camera, and encoded with a dense
keyframe interval so seeking is smooth (`-g 6`).

```bash
# scrub-friendly encode
ffmpeg -i raw.mov -an -vf "scale=1600:-2,fps=30" -c:v libx264 -crf 23 -g 6 \
       -pix_fmt yuv420p -movflags +faststart handshake.mp4
# a webm copy for smaller delivery
ffmpeg -i raw.mov -an -vf "scale=1600:-2,fps=30" -c:v libvpx-vp9 -crf 34 -b:v 0 -g 6 handshake.webm
# poster frame, so the section is not empty before the video loads
ffmpeg -i handshake.mp4 -vf "select=eq(n\,20)" -vframes 1 handshake-poster.jpg
```

Keep it under about 4 MB. In the artifact preview the file has to ship with
the page, which caps at 15 MB per file.

## Drop-in markup

Replace the `<canvas id="tcanvas">` in the Vertrauen section with:

```html
<video id="tvideo" poster="handshake-poster.jpg" muted playsinline preload="metadata" aria-hidden="true">
  <source src="handshake.webm" type="video/webm">
  <source src="handshake.mp4" type="video/mp4">
</video>
```

For plain looping, add `autoplay loop`. For scroll scrubbing, drop the
three.js block and use this instead — it reuses the same `prog()` maths and
the same glow variables the 3D section already drives:

```js
(function(){
  var sec=document.getElementById('vertrauen'), v=document.getElementById('tvideo');
  if(!sec||!v) return;
  if(matchMedia('(prefers-reduced-motion:reduce)').matches){ v.setAttribute('controls',''); return; }
  var dur=0, queued=false;
  v.addEventListener('loadedmetadata',function(){ dur=v.duration; draw(); });
  function prog(){
    var r=sec.getBoundingClientRect(), d=sec.offsetHeight-innerHeight;
    return d<=0?.6:Math.min(1,Math.max(0,-r.top/d));
  }
  function draw(){
    queued=false;
    var p=prog();
    if(dur) v.currentTime=Math.min(dur-.05,p*dur);
    var g=Math.max(0,Math.min(1,(p-.44)/.36)); g=g*g*(3-2*g);
    sec.style.setProperty('--g',(.5+g*.7).toFixed(3));
    sec.style.setProperty('--go',(.16+g*.74).toFixed(3));
  }
  addEventListener('scroll',function(){ if(!queued){ queued=true; requestAnimationFrame(draw); } },{passive:true});
  draw();
})();
```

The CSS already in the page works as is: `#tvideo` takes the same rules as
`#tcanvas` (`position:absolute; inset:0; width:100%; height:100%; object-fit:cover`).

## Prompts, if you do try AI video

Keep shots short, locked-off and close. Avoid asking for a full handshake in
one shot — cut around the grip instead.

- `Extreme close-up, two businessmen in dark navy suits with white shirt cuffs shaking hands, shallow depth of field, warm golden key light from the left, dark navy background, slow subtle motion, cinematic, 35mm, shot on Arri Alexa`
- `Close-up of hands passing a folder of documents across a desk, warm office light, dark blue tones, slow dolly in, shallow depth of field, cinematic`
- `Slow push in on a modern office desk with a laptop showing charts, papers, coffee, warm window light, dark navy and gold colour grade, cinematic, no people`

The last two avoid hands in close-up and will succeed far more often.

## Legal

- Check the licence of any AI tool for **commercial use** — some free tiers forbid it.
- Stock clips: keep the licence document.
- Never use footage or photos from the Google Maps listing.
- Anyone recognisable in the video needs to consent in writing (GDPR / Kunsturhebergesetz).
