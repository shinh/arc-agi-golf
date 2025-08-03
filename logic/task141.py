def p(g):
    for y,r in enumerate(g):
        for x,v in enumerate(r):
            if v:c=v;a=y-x;b=y+x
    h=len(g);w=len(g[0]);o=create(h,w)
    for y in range(h):
        for x in range(w):
            if y-x==a or y+x==b:o[y][x]=c
    return o
