def p(g):
    for t in range(4):
        while 0in g[0]:
            g=g[1:]
        g=[*map(list,zip(*g[::-1]))]
    for t in range(4):
        for r in g:
            for x in range(r.index(r[-1]),len(r)):
                r[x]=r[-1]
        g=[*map(list,zip(*g[::-1]))]
    return g
