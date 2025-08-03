def p(g):
    h=len(g);w=len(g[0]);o=create(h,w)
    for y in range(h):o[y][0]=o[y][w-1]=8
    for x in range(w):o[0][x]=o[h-1][x]=8
    return o
