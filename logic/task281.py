def p(g):
    h=len(g);w=len(g[0])
    d={}
    for y in range(h):
        for x in range(w):
            v=g[y][x]
            if v:d.setdefault(v,[]).append((y,x))
    u=[k for k,v in d.items() if len(v)==1][0]
    uy,ux=d[u][0]
    o=create(h,w)
    yz=[y for k,v in d.items() if k!=u for y,_ in v];xz=[x for k,v in d.items() if k!=u for _,x in v]
    t,b=min(yz),max(yz);l,r=min(xz),max(xz)
    B=g[t][l];C=g[t+1][l+1]
    t=min(t,uy);l=min(l,ux);b=max(b,uy);r=max(r,ux)
    for y in range(t,b+1):
        for x in range(l,r+1):
            o[y][x]=B if y in (t,b) or x in (l,r) else C
    return o
