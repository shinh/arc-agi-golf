def p(g):
    o=[]
    for r in g:
        r=[c for c in r for _ in(0,1)]
        o+=r,r
    return o
