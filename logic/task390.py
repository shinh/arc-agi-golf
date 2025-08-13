# Not golfed yet.
def p(g):
    for o in range(4):
        for r in g:
            if 2in r and 5in r:
                s=r.index(2)
                l=(len(r)-r[::-1].index(2)-s)//2
                r[s-l+1:s-1]=r[s+2:s+l][::-1]
                r[s+2:s+l]=[0]*(l-2)
        g=[*map(list,zip(*g[::-1]))]
    return g
