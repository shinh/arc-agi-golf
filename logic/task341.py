def p(g):
    # bridge shapes with 8
    for k in 0,1:
        sy=99
        sx=ex=ey=0
        for y,r in enumerate(g):
            n=0
            for x,c in enumerate(r):
                if c and n%2<1:
                    if n>1:
                        ex=x
                    n+=1
                if c<1==n%2:
                    if ex<1:
                        sx=x
                    n+=1
            if n>2:
                sy=min(sy,y)
                ey=max(ey,y)

        for r in g[sy+1:ey]:
            r[sx:ex]=[8]*(ex-sx)

        g=[*map(list,zip(*g))]
    return g
