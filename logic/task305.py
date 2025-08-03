def p(g):
    m=max(map(max,g))
    h=len(g);w=len(g[0])
    return [[(x+y)%m+1 for x in range(w)]for y in range(h)]
