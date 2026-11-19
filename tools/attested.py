from grid import *
import numpy as np, json
a=load('charts/16180-reio-script-chart-prn.png')
xs,ys=box(a)
def cl(v):
    r=[];s=v[0];p=v[0]
    for t in v[1:]:
        if t!=p+1:r.append((s,p));s=t
        p=t
    r.append((s,p));return r
print(cl(xs),cl(ys))
