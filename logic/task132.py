def p(g):
    o=[r[:]for r in g]
    for k in{c for r in g for c in r if c}:
        ys=[y for y in range(10)for x in range(10)if g[y][x]==k]
        xs=[x for y in range(10)for x in range(10)if g[y][x]==k]
        for y in range(min(ys),max(ys)+1):
            for x in range(min(xs),max(xs)+1):o[y][x]=k
    return o
