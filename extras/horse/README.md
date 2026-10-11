# Gold horse under the contact form

`img/horse.png` is drawn as Grease Pencil strokes in Blender (5.2) by
`horse_grease_pencil.py`: every stroke tapers like an ink pen, thicker in
the middle and thin at both ends. The site uses the PNG's alpha only, as a
CSS mask, so the ink takes the frame's gold in both modes.

To change the drawing, edit the stroke paths in the script (200 x 220
units, y down; W = outline, D = detail, F = fine hatching), then:

    pip install bpy==5.2.2          # needs libEGL (e.g. apt install libegl1 libegl-mesa0)
    EGL_PLATFORM=surfaceless python horse_grease_pencil.py /tmp/horse.png

and crop/resize the result to img/horse.png (360 px wide, transparent).
The horse is an original drawing of a rearing horse, not the state coat
of arms of North Rhine-Westphalia.

## Current site version: animated in Blender

`horse_animation.py` builds the horse in Blender 5.2 and renders 144
frames (24 fps, 6 s): body, head and hooves as filled 2D curves, legs,
mane strands and tail strands as Grease Pencil strokes. A small rig in the
script turns the body at the hip and each foreleg at shoulder and knee;
mane and tail sway. The horse stands, rears, paws with its forelegs and
comes down again.

    EGL_PLATFORM=surfaceless python horse_animation.py /tmp/frames/f_ 144

Every second frame (12 fps) is cropped to the shared bounding box, scaled
to 128 px and laid in one row in `img/horse-sprite.png` (alpha only, 16
levels). The page uses it as a CSS mask over a gold gradient and steps
through it with `steps(72)`; reduced motion shows the reared frame.
