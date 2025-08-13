# Not golfed yet.
def p(g):
    for o in range(4):
        ref=0
        for r in g:
            if len(set(r))>1 and not(set(r)&{0}):
                ref=r
        if ref:
            for r in g:
                for x in range(len(r)):
                    if r[x]<1:
                        for cx in range(x+1,len(r)):
                            if ref[x]==r[cx]:
                                r[cx]=0
        g=[*map(list,zip(*g[::-1]))]
    return g
