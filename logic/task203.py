def p(g):
    n=len(g);L=[g[i][i] for i in range(n//2)][::-1]
    for i,c in enumerate(L):
        for x in range(i,n-i):g[i][x]=g[-1-i][x]=c
        for y in range(i,n-i):g[y][i]=g[y][-1-i]=c
    return g
