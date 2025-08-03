def p(g):
    for r in g:
        d={}
        for i,v in enumerate(r):
            if v:d.setdefault(v,[]).append(i)
        for v,l in d.items():
            if len(l)>1:r[l[0]:l[-1]+1]=[v]*(l[-1]-l[0]+1)
    w=len(g[0])
    for x in range(w):
        d={}
        for y,r in enumerate(g):
            v=r[x]
            if v:d.setdefault(v,[]).append(y)
        for v,l in d.items():
            if len(l)>1:
                a=l[0];b=l[-1]+1
                for y in range(a,b):g[y][x]=v
    return g
