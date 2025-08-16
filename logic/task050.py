def p(g):
    # fill between 8s hv
    for _ in 0,1:
        for r in g:
            if 8 in r:a=r.index(8)+1;b=~r[::-1].index(8);r[a:b]=[v or 3 for v in r[a:b]]
        g=[*map(list,zip(*g))]
    return g
