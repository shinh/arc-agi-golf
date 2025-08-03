def p(g):
    o=create(3,3);n=len({x for r in g for x,v in enumerate(r) if v})
    for i in range(min(n,3)):o[0][i]=2
    return o
