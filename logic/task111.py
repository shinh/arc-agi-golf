def p(g):
    for y,r in enumerate(g):
        if 5 in r:
            x=r.index(5)-1
            return [g[y+i][x:x+3] for i in range(1,4)]
