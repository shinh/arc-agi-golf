def p(g):# extend from first colored cell to right and down last column
    c=0
    for r in g:
        r[-1]=c
        for x,v in enumerate(r):
            if v:r[x:]=[c:=v]*(len(r)-x);break
    return g

