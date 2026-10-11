import bpy,sys,re,math
OUT=sys.argv[-1]
W=1.0   # outline weight
D=0.62  # detail weight
F=0.42  # fine hatching
STROKES=[
 # head: long noble profile tapering to the muzzle, calm eye, alert ears
 (W,"M116 44 C106 46 96 52 87 60 C81 64 77 67 74 70"),
 (W,"M74 70 C72 73 73 77 77 78"),
 (D,"M77 78 C81 79 85 80 88 80"),
 (D,"M79 82 C82 84 86 84 89 82"),
 (W,"M89 82 C96 84 104 84 109 80 C114 76 116 70 115 64"),
 (F,"M109 62 C105 66 101 70 96 72"),
 (D,"M101 55 C103 53 106 53 107 55 C105 57 103 57 101 55"),
 (F,"M98 51 C101 49 106 48 110 51"),
 (F,"M80 70 C82 69 84 70 84 72"),
 (W,"M115 45 C113 39 113 34 115 29 C118 33 120 38 120 43"),
 (W,"M121 43 C122 38 124 34 127 31 C128 36 127 41 125 46"),
 (F,"M116 35 C117 38 117 40 118 42"),
 # neck front, throat, chest
 (W,"M110 80 C104 86 100 92 99 100 C99 104 100 106 101 108"),
 # crest and back to rump
 (W,"M125 46 C136 53 142 65 143 79 C145 95 151 107 157 119 C161 129 161 139 157 149"),
 # hind leg, rear and weight bearing: hock, slim cannon, hoof
 (W,"M157 149 C164 160 168 172 166 182 C165 188 166 194 168 200"),
 (W,"M168 200 L172 206 L158 206 L160 200"),
 (W,"M160 200 C159 194 158 188 156 182 C152 176 148 172 145 170"),
 # hind leg stepping forward
 (W,"M128 170 C124 178 120 186 116 194 L113 201"),
 (W,"M113 201 L109 206 L121 206 L121 201"),
 (W,"M121 201 C123 195 127 190 133 186 C139 182 142 176 145 171"),
 (W,"M128 170 C124 166 121 161 118 156"),
 # belly
 (W,"M118 156 C110 150 104 142 100 132"),
 # foreleg raised high: forearm, knee, cannon, hoof
 (W,"M101 106 C92 101 82 98 72 98 C68 98 65 100 64 103"),
 (W,"M64 103 C64 108 65 112 67 116"),
 (W,"M67 116 L62 121 L67 125 L72 120"),
 (W,"M72 120 C71 116 71 112 72 108 C80 108 88 110 96 114"),
 # foreleg lower
 (W,"M96 120 C90 122 84 125 79 128 C76 130 75 133 75 136"),
 (W,"M75 136 C75 140 75 143 76 146"),
 (W,"M76 146 L71 151 L77 154 L82 149"),
 (W,"M82 149 C82 145 82 141 83 137 C88 134 94 130 100 128"),
 # mane: organised, flowing strands
 (D,"M116 44 C112 45 109 47 107 50"),
 (D,"M121 45 C129 45 135 49 139 55"),
 (D,"M124 51 C132 55 138 62 141 71"),
 (D,"M127 59 C135 64 141 73 143 83"),
 (D,"M130 69 C138 75 144 85 146 95"),
 (D,"M134 81 C142 87 148 97 150 107"),
 (D,"M139 93 C147 99 152 109 153 119"),
 (F,"M126 64 C130 67 133 71 134 75"),
 (F,"M131 82 C134 86 137 90 138 95"),
 # tail: raised and curling
 (W,"M155 132 C164 122 166 110 162 98 C160 90 164 82 172 80 C178 79 182 84 179 89"),
 (D,"M156 138 C168 128 172 114 169 102 C168 94 171 88 177 86"),
 (D,"M157 144 C172 136 178 120 176 106"),
 (D,"M158 150 C174 146 182 132 182 118"),
 (F,"M158 156 C170 158 180 152 186 140"),
 # anatomy: shoulder, elbow, flank, thigh, gaskin
 (D,"M103 100 C110 104 116 106 123 106"),
 (D,"M118 132 C122 136 127 138 133 138"),
 (D,"M131 151 C137 147 141 140 143 132"),
 (F,"M140 157 L144 162 M144 155 L148 160 M148 153 L152 158"),
 (F,"M106 88 L113 86 M107 92 L114 90 M108 96 L115 94"),
 (F,"M150 176 L155 179 M151 182 L156 185"),
 (F,"M66 104 L69 106 M78 102 L80 105"),
 # ground
 (0.5,"M42 207 L188 207"),
]
def sample(d,n_per=28):
    toks=re.findall(r"[MCL]|-?\d+\.?\d*",d)
    pts=[];i=0;cur=None;segs=[];cmd=None
    out=[]  # list of polylines (M starts new)
    while i<len(toks):
        t=toks[i]
        if t in "MCL": cmd=t;i+=1;continue
        if cmd=="M":
            cur=(float(toks[i]),float(toks[i+1]));i+=2;out.append([cur]);cmd="L"
        elif cmd=="L":
            p=(float(toks[i]),float(toks[i+1]));i+=2
            for k in range(1,9): out[-1].append((cur[0]+(p[0]-cur[0])*k/8,cur[1]+(p[1]-cur[1])*k/8))
            cur=p
        elif cmd=="C":
            c1=(float(toks[i]),float(toks[i+1]));c2=(float(toks[i+2]),float(toks[i+3]));p=(float(toks[i+4]),float(toks[i+5]));i+=6
            for k in range(1,n_per+1):
                s=k/n_per;a=(1-s)**3;b=3*(1-s)**2*s;c=3*(1-s)*s*s;e=s**3
                out[-1].append((a*cur[0]+b*c1[0]+c*c2[0]+e*p[0],a*cur[1]+b*c1[1]+c*c2[1]+e*p[1]))
            cur=p
    return out
bpy.ops.wm.read_factory_settings(use_empty=True)
sc=bpy.context.scene
gp=bpy.data.grease_pencils.new("Horse")
ob=bpy.data.objects.new("Horse",gp); sc.collection.objects.link(ob)
mat=bpy.data.materials.new("ink"); bpy.data.materials.create_gpencil_data(mat)
mat.grease_pencil.color=(0,0,0,1); gp.materials.append(mat)
d=gp.layers.new("ink").frames.new(1).drawing
lines=[]
for w,path in STROKES:
    for pl in sample(path): lines.append((w,pl))
d.add_strokes([len(pl) for w,pl in lines])
BASE=0.0115
for st,(w,pl) in zip(d.strokes,lines):
    n=len(pl)
    for j,(x,y) in enumerate(pl):
        t=j/(n-1) if n>1 else .5
        taper=0.16+0.84*(math.sin(math.pi*t)**0.65)
        p=st.points[j]; p.position=((x-115)/100,0,-(y-115)/100); p.radius=BASE*w*taper
cam=bpy.data.cameras.new("C"); cam.type='ORTHO'; cam.ortho_scale=1.9
co=bpy.data.objects.new("C",cam); sc.collection.objects.link(co); co.location=(0,-5,0); co.rotation_euler=(math.pi/2,0,0); sc.camera=co
sc.render.resolution_x=1000; sc.render.resolution_y=1000; sc.render.film_transparent=True
sc.render.engine='BLENDER_EEVEE'; sc.view_settings.view_transform='Standard'
sc.render.filepath=OUT; bpy.ops.render.render(write_still=True)
