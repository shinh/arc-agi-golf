# draw diagonals from isolated colors
def p(g):
    h=len(g);w=len(g[0]);d={}
    for y,r in enumerate(g):
        for x,v in enumerate(r):d.setdefault(v,[]).append((y,x))
    r=[]
    for c,ps in d.items():
        l=[g[ny][nx]for y,x in ps for ny in range(max(0,y-1),min(h,y+2))for nx in range(max(0,x-1),min(w,x+2))if(ny,nx)!=(y,x)]
        if c not in l:r.append((c,max(set(l),key=l.count),ps))
    a,ca,pa=r[0];b,cb,pb=r[-1]
    S={(Y,X)for y,x in pa+pb for Y in range(h)for X in range(w)if abs(Y-y)==abs(X-x)}
    for y,x in S:
        v=g[y][x]
        if v==ca:g[y][x]=a
        if v==cb:g[y][x]=b
    return g
