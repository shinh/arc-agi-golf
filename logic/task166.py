def p(g):
    x0=y0=99;x1=y1=0
    for y,r in enumerate(g):
        for x,c in enumerate(r):
            if c==8:
                if x<x0:x0=x
                if x>x1:x1=x
                if y<y0:y0=y
                if y>y1:y1=y
    for y in range(y0,y1+1):
        r=g[y]
        for x in range(x0,x1+1):
            if not r[x]:r[x]=2
    return g
