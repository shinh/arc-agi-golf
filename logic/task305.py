def p(g):
    m=max(map(max,g))
    return [[(x+y)%m+1 for x in range(16)]for y in range(16)]
