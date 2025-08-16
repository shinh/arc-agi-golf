def p(g):
    # fill segments horizontally then vertically
    for _ in 0,1:
        for r in g:
            for c in r:
                if c:
                    a=r.index(c);b=len(r)-r[::-1].index(c);r[a:b]=[c]*(b-a)
        g=[*map(list,zip(*g))]
    return g
