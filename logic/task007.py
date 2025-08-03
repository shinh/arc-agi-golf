def p(g):
    h=len(g);w=len(g[0])
    d={}
    for y in range(h):
        for x in range(w):
            c=g[y][x]
            if c:d[y+x]=c
    s=[d[k] for k in sorted(d)];k=min(d)
    return [[s[(y+x-k)%3] for x in range(w)] for y in range(h)]
