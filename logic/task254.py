def p(g):
    cnt=[sum(r[x]==5 for r in g) for x in range(9)]
    cmax=cnt.index(max(cnt))
    cmin=min((c,i) for i,c in enumerate(cnt) if c)[1]
    o=create(9,9)
    for y in range(9):
        if g[y][cmax]==5:o[y][cmax]=1
        if g[y][cmin]==5:o[y][cmin]=2
    return o
