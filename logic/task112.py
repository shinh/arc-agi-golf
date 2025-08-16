def p(g):
    # mirror each color around the center of the only 2x2 block
    h=len(g);w=len(g[0])
    for y in range(h-1):
        for x in range(w-1):
            c=g[y][x]
            if c==g[y][x+1]==g[y+1][x]==g[y+1][x+1]!=0 and sum(r.count(c)for r in g)==4:S=y*2+1;T=x*2+1
    for y,r in enumerate(g):
        for x,c in enumerate(r):
            if c:
                for Y in y,S-y:
                    if 0<=Y<h:
                        for X in x,T-x:
                            if 0<=X<w:g[Y][X]=c
    return g
