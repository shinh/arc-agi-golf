def p(g):
    d={}
    for y,r in enumerate(g):
        for x,v in enumerate(r):
            if v:d.setdefault(v,[]).append((y,x))
    ys,xs=zip(*min(d.values(),key=len))
    return [r[min(xs):max(xs)+1] for r in g[min(ys):max(ys)+1]]
