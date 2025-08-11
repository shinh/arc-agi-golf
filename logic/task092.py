def p(g):
    for o in range(4):
        for c in range(1,10):
            for r in g:
                if c in r:
                    a=r.index(c)
                    b=len(r)-r[::-1].index(c)-1
                    r[a:b+1]=[c]*(b-a+1)
        g=[*map(list,zip(*g[::-1]))]
    return g
