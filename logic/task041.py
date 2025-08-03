def p(g):
    for r in g:
        for c in set(r):
            if c:i=r.index(c);j=len(r)-r[::-1].index(c);r[i:j]=[c]*(j-i)
    return g
