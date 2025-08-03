def p(g):
    if all(g[0])and all(g[-1]):a,b,n=g[0][0],g[-1][0],0
    else:a,b,n=g[0][0],g[0][-1],1
    for y,r in enumerate(g):
        for x,v in enumerate(r):
            if v==3:r[x]=(a,b)[(y,x)[n]>4]
    return g
