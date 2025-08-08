def p(g):
    # We remove only a single pixel every 4 iterations.
    for o in range(44):
        w=len(g[0]);y=1
        for y in range(len(g)):
            for x in range(w-1):
                if g[y][x-1]+g[y][x+1]==0and g[y-1][x]!=g[y][x]and g[y][x]*g[y-1][x]:
                    g=g[:y]+g[y+1:]+[[0]*w]
        g=[list(r)for r in zip(*g[::-1])]
    return g
