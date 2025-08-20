def p(g):
    for o in[0]*4:
        for r in g:
            if r[0]:
                r[r.index(8)]=r[0]
        g=[*map(list,zip(*g[::-1]))]
    return g
