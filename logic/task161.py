def p(g):
    a=sum(g,[]);L=[r[0] for r in g];R=[r[-1] for r in g];T=g[0];B=g[-1]
    c=min({*([*L,*R,*T,*B])}-{0},key=lambda x:a.count(x) if (x in L and x in R) or (x in T and x in B) else 1e9)
    w=len(g[0]);o=[[0]*w for _ in g]
    for y,r in enumerate(g):
        if r[0]==r[-1]==c:o[y]=[c]*w
    for x in range(w):
        if g[0][x]==g[-1][x]==c:
            for r in o:r[x]=c
    return o
