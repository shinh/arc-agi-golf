def p(g):
    r=len(g)-2;w=len(g[0]);a=next(i for i,c in enumerate(g[r]) if c);b=w-1-next(i for i,c in enumerate(g[r][::-1]) if c);y=g[-1][w//2]
    for i in range(1,r+1):
        if a-i>=0:g[r-i][a-i]=y
        if b+i<w:g[r-i][b+i]=y
    return g
