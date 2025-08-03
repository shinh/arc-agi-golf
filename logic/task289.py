def p(g):
    f=len({c for r in g for c in r if c});n=len(g);m=len(g[0]);o=[[0]* (m*f) for _ in range(n*f)]
    for y,r in enumerate(g):
        for x,c in enumerate(r):
            for i in range(f):
                for j in range(f):
                    o[y*f+i][x*f+j]=c
    return o
