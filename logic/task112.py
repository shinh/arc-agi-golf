def p(g):
    h=len(g);w=len(g[0]);bg=0;m={}
    for y,row in enumerate(g):
        for x,c in enumerate(row):
            if c:m.setdefault(c,[]).append((y,x))
    for s in m.values():
        if len(s)==4:
            ys=[y for y,_ in s];xs=[x for _,x in s]
            if max(ys)-min(ys)==max(xs)-min(xs)==1:
                S=min(ys)+max(ys);T=min(xs)+max(xs);break
    r=[r[:]for r in g]
    for y,row in enumerate(g):
        for x,c in enumerate(row):
            if c:
                for Y,X in((y,x),(S-y,x),(y,T-x),(S-y,T-x)):
                    if 0<=Y<h and 0<=X<w:r[Y][X]=c
    return r
