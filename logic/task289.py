def p(g):
    f=len({c for r in g for c in r if c});o=[[0]*(3*f) for _ in range(3*f)]
    for y,r in enumerate(g):
        for x,c in enumerate(r):
            for i in range(f):
                for j in range(f):
                    o[y*f+i][x*f+j]=c
    return o
