# Not golfed yet.
def p(g):
    for _ in[0]*4:
        if ref:=next((r for r in g if len({*r})-1 and 0 not in r),0):
            for r in g:r[:]=[v*(v not in[a for a,b in zip(ref,r)if b<1])for v in r]
        g=[*map(list,zip(*g[::-1]))]
    return g
