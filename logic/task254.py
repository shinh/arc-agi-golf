def p(g):
    h=len(g);w=len(g[0])
    cnt=[sum(r[x]==5 for r in g) for x in range(w)]
    cmax=cnt.index(max(cnt))
    cmin=min((c,i) for i,c in enumerate(cnt) if c)[1]
    o=create(h,w)
    for y in range(h):
        if g[y][cmax]==5:o[y][cmax]=1
        if g[y][cmin]==5:o[y][cmin]=2
    return o
