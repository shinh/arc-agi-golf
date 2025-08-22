def p(g):
    # fill between 8s hv
    for _ in 0,0:
        for r in g:
            try:a=r.index(8)+1;b=r.index(8,a);r[a:b]=[3]*(b-a)
            except:0
        g=[*map(list,zip(*g))]
    return g

