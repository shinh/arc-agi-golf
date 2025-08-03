def p(g):
    n=len({c for r in g for c in r if c})
    o=[]
    for r in g:
        t=[c for c in r for _ in range(n)]
        o+=[t]*n
    return o
