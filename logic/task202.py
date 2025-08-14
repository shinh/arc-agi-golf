# Not golfed yet.
def p(g):
    for _ in[0]*4:
        ref=0
        for r in g:
            if len({*r})-1 and 0 not in r:ref=r
        if ref:
            for r in g:
                s=[]
                for x,v in enumerate(r):
                    if v<1:s+=ref[x],
                    elif v in s:r[x]=0
        g=[*map(list,zip(*g[::-1]))]
    return g
