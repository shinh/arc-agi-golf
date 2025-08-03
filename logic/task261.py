def p(g):
    h=len(g);w=len(g[0]);o=create(h,w)
    for y in range(h-1):
        for x in range(w):
            if g[y][x]==8:o[y+1][x]=2
    return o
