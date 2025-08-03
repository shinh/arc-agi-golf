def p(g):
    t=list(zip(*g))
    if sum(len(set(c))for c in t)<sum(len(set(r))for r in g):
        m=[max(c,key=c.count)for c in t]
        return [m[:] for _ in g]
    w=len(g[0])
    return [[max(r,key=r.count)]*w for r in g]
