def p(g):
    #l
    for u in zip(*g),g:
        g=[*map(list,zip(*g))]
        for r,p in zip(g,u):
            if 8 in p:a,b=p.index(8),len(p)-p[::-1].index(8);r[a:b]=[8]*(b-a)
    return g
