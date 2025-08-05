def p(g):
    w=len(g[0])
    for r in g:
        if 4 in r:
            d=r.index(4)<w//2
            break
    for i in range(3):
        s=g[i][3:6][::-1]
        if d:g[i][:3]=s
        else:g[i][-3:]=s
    return g
