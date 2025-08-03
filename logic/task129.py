def p(g):
    d={}
    for r in g:
        for v in r:d[v]=d.get(v,0)+1
    m=max(d,key=d.get)
    return [[m]*3 for _ in g]
