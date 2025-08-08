def p(g):
    h=len(g);w=len(g[0])
    o=[r for r in g]
    for y,r in enumerate(g):
        for x,c in enumerate(r):
            if c:
                for i in range(x,w):o[y][i]=c
                for j in range(y,h):o[j][w-1]=c
    return o
