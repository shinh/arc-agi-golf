def p(g):
    for o in range(4):
        e=[r.index(8)for r in g if 8 in r]
        if e:
            e,=e
            for r in g:
                f=n=0
                for x,c in enumerate(r):
                    if c:
                        if f<1:
                            f=c
                        elif n<1:
                            n=c
                    elif n and x<e:
                        r[x-1:e]=[n]*(e-x+1)
                        r[e]=f
                        n=0

        g=[*map(list,zip(*g[::-1]))]
    return g
