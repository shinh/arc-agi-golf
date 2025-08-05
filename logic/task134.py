def p(g):
    h=20;w=24
    cols=[c for c in {v for r in g for v in r} if c]
    def iso(c):
        for y,r in enumerate(g):
            for x,v in enumerate(r):
                if v==c and all(not(0<=y+dy<h and 0<=x+dx<w and g[y+dy][x+dx]==c) for dx,dy in((1,0),(-1,0),(0,1),(0,-1))):
                    return 1
        return 0
    a,b2=cols if not iso(cols[0]) else cols[::-1]
    ys=[y for y,r in enumerate(g) for x,v in enumerate(r) if v==a]
    xs=[x for y,r in enumerate(g) for x,v in enumerate(r) if v==a]
    t,bh=min(ys),max(ys);l,rh=min(xs),max(xs)
    sub=[row[l:rh+1] for row in g[t:bh+1]]
    for y,r in enumerate(sub):
        for x,v in enumerate(r):
            if v==a:r[x]=b2
            elif v==b2:r[x]=0
    H,W=len(sub),len(sub[0])
    for f in range(min(H,W)-(H==W),1,-1):
        if H%f or W%f:continue
        d=[r[::f] for r in sub[::f]]
        if [[d[y//f][x//f] for x in range(W)] for y in range(H)]==sub:
            return d
    return sub
