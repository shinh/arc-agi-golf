def p(g):
    # draw diagonals
    w=len(d:=g[-2]);a=d.index(max(d))
    for r in g[-3::-1]:
        if a:a-=1;r[a]=r[w+~a]=g[-1][w//2]
    return g

