def p(g):
    b=[r[:3]for r in g[:3]]
    for y,x in [(y,x)for y,r in enumerate(g)for x,v in enumerate(r)if v==1]:
        for dy,r in enumerate(b):
            for dx,v in enumerate(r):g[y+dy-1][x+dx-1]=v
    return g
