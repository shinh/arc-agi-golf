def p(g):
    o=[]
    for r in g:
        R=[c for c in r for _ in(0,1,2)]
        o+= [R[:] for _ in(0,1,2)]
    return o
