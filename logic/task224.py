def p(g):# draw inner color rectangle just inside 5s
    y,x=zip(*[(y,x)for y,r in enumerate(g)for x,c in enumerate(r)if c==5]);t=min(y)+1;b=max(y);l=min(x)+1;r=max(x);c=next(g[y][x]for y in range(t,b)for x in range(l,r)if g[y][x]%5)
    for x in range(l,r):g[t][x]=g[b-1][x]=c
    for y in range(t,b):g[y][l]=g[y][r-1]=c
    return g
