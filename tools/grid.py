from PIL import Image
import numpy as np
def load(p): return np.array(Image.open(p).convert('RGB')).astype(int)
def box(a):
    cy=(abs(a[:,:,0]-8)<12)&(a[:,:,1]>235)&(abs(a[:,:,2]-200)<20)
    # main box only: exclude small right-hand box
    cols=cy.sum(0); rows=cy.sum(1)
    xs=np.where(cols>len(cols)*0.4)[0]; ys=np.where(rows>len(rows)*0.3)[0]
    return xs,ys
def orange_lines(a,x0,x1,y0,y1):
    o=(a[:,:,0]>240)&(abs(a[:,:,1]-104)<20)&(a[:,:,2]<30)
    vx=np.where(o[y0:y1,x0:x1].sum(0)>(y1-y0)*0.5)[0]+x0
    hy=np.where(o[y0:y1,x0:x1].sum(1)>(x1-x0)*0.5)[0]+y0
    return vx,hy
if __name__=='__main__':
    a=load('charts/16176-1-chart-i-all.png')
    xs,ys=box(a); print(xs.min(),xs.max(),ys.min(),ys.max(), len(xs),len(ys))
    print(xs[:20],ys[:20])
    # main box inner
    # find edges: vertical cyan lines are columns with many cyan; list clusters
    def cl(v):
        r=[];s=v[0];p=v[0]
        for t in v[1:]:
            if t!=p+1:r.append((s,p));s=t
            p=t
        r.append((s,p));return r
    print(cl(xs),cl(ys))
