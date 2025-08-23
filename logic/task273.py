def p(g):
    # fill rectangles enclosed by 4s
    d={}
    for y,r in enumerate(g):
        if 4in r:
            for R in g[d.get((a:=r.index(4),b:=9-r[::-1].index(4)),y)+1:y]:R[a+1:b]=[2]*~(a-b)
            d[a,b]=y
    return g
