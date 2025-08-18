def p(g):
    for o in range(4):
        for r,nr in zip(g,g[1:]):
            n=r.count(5)
            if n:
                s=r.index(5)+1
                e=[9-r[::-1].index(5),10][n<2 and nr.index(5)+1==s]
                if n<3:
                    r[s:e]=[8]*(e-s)

        g=[*map(list,zip(*g[::-1]))]
    return g
