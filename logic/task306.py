def p(g):
    h=len(g);w=len(g[0])
    rs=[0]+[i+1 for i,r in enumerate(g)if all(v==4 for v in r)]
    cs=[0]+[j+1 for j in range(w)if all(r[j]==4 for r in g)]
    o=[r for r in g]
    for y,row in enumerate(g):
        for x,v in enumerate(row):
            if v and v!=4:
                sy=max(r for r in rs if r<=y)
                sx=max(c for c in cs if c<=x)
                for ry in rs:
                    for cx in cs:
                        o[y-sy+ry][x-sx+cx]=v
    return o
