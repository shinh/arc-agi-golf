def p(g):
    # draw diagonals
    d=g[-2];w=len(d);y=g[-1][w//2]
    a=next(i for i in range(w)if d[i]);b=w-1-next(i for i in range(w)if d[~i])
    for i in range(1,len(g)-1):
        if a>=i:g[-2-i][a-i]=y
        if b+i<w:g[-2-i][b+i]=y
    return g
