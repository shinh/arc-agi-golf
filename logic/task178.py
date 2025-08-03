def p(g):
    h=[];p=None
    for c in zip(*g):
        if c!=p:h+=c,;p=c
    g=[list(r)for r in zip(*h)]
    o=[];p=None
    for r in g:
        if r!=p:o+=r,;p=r
    return o
