# Gold rearing horse, built and animated as Grease Pencil in Blender.
# Geometry in a 120 x 110 box (y down, ground at y=94.5); the rig is done
# here in Python: body turns at the hip, forelegs at shoulder and knee,
# mane and tail are separate strands that sway.
import bpy, math, re, sys
OUT=sys.argv[-2]; NFR=int(sys.argv[-1])
FPS=24
def bez(d,n=10):
    toks=re.findall(r"[MCLZ]|-?\d+\.?\d*",d); out=[];cur=None;cmd=None;i=0
    while i<len(toks):
        t=toks[i]
        if t in "MCLZ":
            cmd=t;i+=1
            if t=="Z": cmd=None
            continue
        if cmd=="M": cur=(float(toks[i]),float(toks[i+1]));i+=2;out.append(cur);cmd="L"
        elif cmd=="L":
            p=(float(toks[i]),float(toks[i+1]));i+=2
            for k in range(1,5): out.append((cur[0]+(p[0]-cur[0])*k/4,cur[1]+(p[1]-cur[1])*k/4))
            cur=p
        elif cmd=="C":
            c1=(float(toks[i]),float(toks[i+1]));c2=(float(toks[i+2]),float(toks[i+3]));p=(float(toks[i+4]),float(toks[i+5]));i+=6
            for k in range(1,n+1):
                s=k/n;a=(1-s)**3;b=3*(1-s)**2*s;c=3*(1-s)*s*s;e=s**3
                out.append((a*cur[0]+b*c1[0]+c*c2[0]+e*p[0],a*cur[1]+b*c1[1]+c*c2[1]+e*p[1]))
            cur=p
    return out
BODY=bez("M38 48 C42 43 50 41 58 41 L80 41 C88 41 94 44 95 50 C96 57 93 63 86 65 C74 67 60 67 50 66 C44 65 39 63 37 58 C36 54 36 51 38 48")
HEAD=bez("M39 51 C35 46 33 40 31 35 C28 36 25 38 22 39 L15 39 C12 39 11 35 13 33 L22 25 C25 22 28 20 31 19 L30 12 L34 18 L36 11 L37 19 C44 23 52 32 58 41 L50 45")
CREST=bez("M37 19 C44 23 52 32 58 41",12)
def rot(p,o,a):
    a=math.radians(a); x,y=p[0]-o[0],p[1]-o[1]
    return (o[0]+x*math.cos(a)-y*math.sin(a), o[1]+x*math.sin(a)+y*math.cos(a))
def ease(t): return 0.5-0.5*math.cos(math.pi*max(0,min(1,t)))
def pose(f):
    """rear amount 0..1, paw phase, time"""
    t=f/FPS
    if t<1.0: r=0
    elif t<2.0: r=ease(t-1.0)
    elif t<3.6: r=1
    elif t<4.6: r=1-ease(t-3.6)
    else: r=0
    paw=0 if r<0.9 else min(1,(r-0.9)/0.1)
    return r,paw,t
def frame_geo(f):
    r,paw,t=pose(f)
    HIP=(82,60)
    A=34*r
    B=lambda p: rot(p,HIP,A)
    polys=[]   # filled shapes
    lines=[]   # (points, width)
    polys.append([B(p) for p in BODY]); polys.append([B(p) for p in HEAD])
    # hind legs stay planted
    lines.append((bez("M85 58 C89 66 91 73 90 80 L87 92"),4.6)); lines.append((bez("M77 60 C80 67 81 74 80 80 L76 92"),4.2))
    polys.append(bez("M83 91 L91 91 L90 94.5 L83 94.5")); polys.append(bez("M72 91 L80 91 L79 94.5 L72 94.5"))
    # forelegs: shoulder and knee, pawing alternately while reared
    w=2*math.pi*2.2*t
    for k,(sh,kn,ft,ux,lw,uw) in enumerate([((42,60),(42,76),(42,91),1.0,3.6,5.2),((48,61),(49,77),(49,91),0.8,3.4,4.8)]):
        ph=0 if k==0 else math.pi
        up=(68*ux)*r + paw*10*math.sin(w+ph)
        lo=(-112*(0.85 if k else 1))*r + paw*22*math.sin(w+ph+0.6)
        knee=rot(kn,sh,up); foot=rot(rot(ft,kn,lo),sh,up)
        hoof=[rot(rot(p,kn,lo),sh,up) for p in [(ft[0]-4,ft[1]),(ft[0]+4,ft[1]),(ft[0]+3,ft[1]+3.5),(ft[0]-4,ft[1]+3.5)]]
        lines.append(([B(sh),B(knee)],uw)); lines.append(([B(knee),B(foot)],lw)); polys.append([B(p) for p in hoof])
    # mane: strands along the crest, flowing back and swaying
    sway=1+1.6*r
    for i in range(0,len(CREST),2):
        x,y=CREST[i]; s=i/len(CREST)
        pts=[]
        for j in range(7):
            u=j/6; L=7+5*(1-abs(s-.4))
            wave=math.sin(2*math.pi*(1.3*t)-s*4-u*2.2)*sway*u*2.2
            pts.append((x+ u*L*0.9 + wave*0.3, y+ u*L*0.55 + wave))
        lines.append(([B(p) for p in pts],1.6))
    # tail: strands from the croup, swaying
    for k in range(6):
        pts=[]
        for j in range(10):
            u=j/9; L=24+k*1.5
            wave=math.sin(2*math.pi*(1.1*t)-u*3-k*0.5)*(1.5+3*u)*(1+0.6*r)
            pts.append((93+u*(6+k*1.6)+wave*0.5, 47+u*L+wave*0.4))
        lines.append(([B(p) for p in pts],2.6-k*0.25))
    return polys,lines
bpy.ops.wm.read_factory_settings(use_empty=True)
sc=bpy.context.scene; sc.render.fps=FPS
SC=1/50
def P(p): return ((p[0]-60)*SC,0,-(p[1]-41)*SC)
# filled shapes: 2D curve objects, one per polygon slot
mat=bpy.data.materials.new("solid")
def make_curve(n,name):
    cu=bpy.data.curves.new(name,'CURVE'); cu.dimensions='2D'; cu.fill_mode='BOTH'
    sp=cu.splines.new('POLY'); sp.points.add(n-1); sp.use_cyclic_u=True
    o=bpy.data.objects.new(name,cu); o.rotation_euler=(math.pi/2,0,0); sc.collection.objects.link(o)
    cu.materials.append(mat); return cu
polys0,lines0=frame_geo(0)
curves=[make_curve(len(p),"poly%d"%i) for i,p in enumerate(polys0)]
# strokes: one Grease Pencil drawing, rebuilt every frame
gp=bpy.data.grease_pencils.new("Hair"); ob=bpy.data.objects.new("Hair",gp); sc.collection.objects.link(ob)
ms=bpy.data.materials.new("ink"); bpy.data.materials.create_gpencil_data(ms); ms.grease_pencil.color=(0,0,0,1); gp.materials.append(ms)
layer=gp.layers.new("ink"); drawing=layer.frames.new(1).drawing
cam=bpy.data.cameras.new("C"); cam.type='ORTHO'; cam.ortho_scale=2.4
co=bpy.data.objects.new("C",cam); sc.collection.objects.link(co); co.location=(0,-5,0); co.rotation_euler=(math.pi/2,0,0); sc.camera=co
sc.render.resolution_x=360; sc.render.resolution_y=330; sc.render.film_transparent=True
sc.render.engine='BLENDER_EEVEE'; sc.view_settings.view_transform='Standard'
sc.render.image_settings.file_format='PNG'; sc.render.image_settings.color_mode='RGBA'
try:
    sc.eevee.taa_render_samples=8
except Exception: pass
import os
for f in range(NFR):
    if os.path.exists(OUT+"%04d.png"%(f+1)): continue
    polys,lines=frame_geo(f)
    for cu,poly in zip(curves,polys):
        for j,p in enumerate(poly):
            x,_,z=P(p); cu.splines[0].points[j].co=(x,z,0,1)
    if len(drawing.strokes): drawing.remove_strokes()
    drawing.add_strokes([len(l[0]) for l in lines])
    for st,(pts,wd) in zip(drawing.strokes,lines):
        n=len(pts)
        for j,p in enumerate(pts):
            u=j/(n-1) if n>1 else 0
            taper=1.0 if n<=2 else (1-0.85*u)
            st.points[j].position=P(p); st.points[j].radius=wd/2*SC*taper
    sc.render.filepath=OUT+"%04d.png"%(f+1)
    bpy.ops.render.render(write_still=True)
