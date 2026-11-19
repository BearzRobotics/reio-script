from grid import *
import numpy as np, potrace, csv
from PIL import Image, ImageFilter
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.pens.cu2quPen import Cu2QuPen
from fontTools.ttLib import TTFont

img=Image.open('charts/16176-1-chart-i-all.png').convert('L')
g=np.array(img)
X0,X1,Y0,Y1=272,8663,271,5060
px=(X1-X0)/63; py=(Y1-Y0)/36
att=np.load('att.npy')
COLG=[5,5,7,6,6,5,4,5,5,6,4,3,2]; ROWG=[4,6,2,2,4,8,10]
def idx(groups):
    out=[]
    for gi,n in enumerate(groups):
        for k in range(n): out.append((gi+1,k+1))
    return out
CI=idx(COLG); RI=idx(ROWG)
UP=8; UPM=1000; S=UPM/px; DESC=150
def area(pts):
    return sum(pts[i][0]*pts[(i+1)%len(pts)][1]-pts[(i+1)%len(pts)][0]*pts[i][1] for i in range(len(pts)))/2
def draw(pen,curve,fx,fy,hole):
    segs=curve.segments
    pts=[curve.start_point]+[s.end_point for s in segs]
    # signed area in font space; want outer CW (neg), hole CCW (pos)
    ar=area([(fx((q.x,q.y)),fy(q.y)) for q in pts])
    rev=(ar>0) if not hole else (ar<0)
    start=curve.start_point
    ops=[]
    cur=start
    for s in segs:
        if s.is_corner: ops.append(('l',[s.c,s.end_point]))
        else: ops.append(('c',[s.c1,s.c2,s.end_point]))
    P=lambda p:(fx((p.x,p.y)),fy(p.y))
    if not rev:
        pen.moveTo(P(start))
        for k,pp in ops:
            if k=='l': pen.lineTo(P(pp[0])); pen.lineTo(P(pp[1]))
            else: pen.curveTo(P(pp[0]),P(pp[1]),P(pp[2]))
        pen.closePath()
    else:
        # reverse path
        pts_list=[start]
        segsr=[]
        prev=start
        for k,pp in ops:
            segsr.append((k,prev,pp)); prev=pp[-1]
        pen.moveTo(P(prev))
        for k,pv,pp in reversed(segsr):
            if k=='l': pen.lineTo(P(pp[0])); pen.lineTo(P(pv))
            else: pen.curveTo(P(pp[1]),P(pp[0]),P(pv))
        pen.closePath()
def walk(pen,curve,fx,fy,depth=0):
    draw(pen,curve,fx,fy,depth%2==1)
    for ch in (curve.children or []): walk(pen,ch,fx,fy,depth+1)

glyphs={}; order=['.notdef','space']; rows=[]
cmap={0x20:'space'}
sq=TTGlyphPen(None)
adv={}
for r in range(36):
    for c in range(63):
        xa,xb=int(round(X0+c*px)),int(round(X0+(c+1)*px)); ya,yb=int(round(Y0+r*py)),int(round(Y0+(r+1)*py))
        cell=Image.fromarray(g[ya:yb,xa:xb])
        W,H=cell.size
        big=cell.resize((W*UP,H*UP),Image.BICUBIC).filter(ImageFilter.GaussianBlur(UP*0.55))
        bm=np.array(big)<20
        bm=np.pad(bm,2)
        name=f'r{r+1:02d}c{c+1:02d}'
        pen=TTGlyphPen(None)
        cpen=Cu2QuPen(pen,max_err=1.0)
        if bm.any():
            pl=potrace.Bitmap(~bm).trace(turdsize=12,alphamax=1.25,opticurve=True,opttolerance=1.0)
            # pixel (px) -> font
            fx=lambda p:(p[0]-2)/UP*S
            fy=lambda y:UPM-DESC-(y-2)/UP*S
            for cv in pl:
                pp=[cv.start_point]+[q.end_point for q in cv.segments]
                w=max(p.x for p in pp)-min(p.x for p in pp); h=max(p.y for p in pp)-min(p.y for p in pp)
                if min(w,h)<40: continue
                walk(cpen,cv,fx,fy)
        glyphs[name]=pen.glyph()
        u=0xE000+r*63+c; cmap[u]=name; order.append(name)
        cg,ck=CI[c]; rg,rk=RI[r]
        rows.append([f'U+{u:04X}',name,r+1,c+1,rg,rk,cg,ck,'yes' if att[r,c] else 'no','yes' if bm.any() else 'no'])
    print(r,end=' ',flush=True)
adv=UPM
fb=FontBuilder(UPM,isTTF=True)
fb.setupGlyphOrder(order)
fb.setupCharacterMap(cmap)
empty=TTGlyphPen(None).glyph()
gl={'.notdef':empty,'space':empty}; gl.update(glyphs)
fb.setupGlyf(gl)
fb.setupHorizontalMetrics({n:(adv,0) for n in order})
fb.setupHorizontalHeader(ascent=UPM-DESC,descent=-DESC)
fb.setupNameTable({'familyName':'RE_iO Script','styleName':'Regular'})
fb.setupOS2(sTypoAscender=UPM-DESC,sTypoDescender=-DESC,usWinAscent=UPM-DESC,usWinDescent=DESC)
fb.setupPost()
fb.save('REiO-Script.ttf')
with open('REiO-Script-glyphs.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(['codepoint','glyph','row','col','row_group','row_in_group','col_group','col_in_group','attested_in_speech','has_ink']); w.writerows(rows)
print('done',sum(1 for r in rows if r[-1]=='no'),'blank cells')
