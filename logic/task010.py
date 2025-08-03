def p(g):
    d={}
    for r in g:
        for i,v in enumerate(r):
            if v==5:r[i]=d.setdefault(i,len(d)+1)
    return g
