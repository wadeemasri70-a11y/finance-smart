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
