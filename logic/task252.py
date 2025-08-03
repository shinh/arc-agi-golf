def p(g):
    d={}
    for y,r in enumerate(g):
        for x,v in enumerate(r):
            if v:
                k=y-x
                if d.get(k):r[x]=4;d[k]=0
                else:d[k]=1
    return g
