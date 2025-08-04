def p(g):
    n=len(g)
    for y in range(n):
        for x in range(n):
            c=g[y][x]
            if c:g[y][x]=g[n-1-y][x]=g[y][n-1-x]=g[n-1-y][n-1-x]=c
    for _ in range(4):
        t=[(y,x,g[y][x])for y in range(n)for x in range(n)if g[y][x]and y+1<x<n-2-y and x%2]
        for y,x,c in t:
            for j in range(x,n-2-y,2):g[y][j]=c
        g=[list(r)for r in zip(*g[::-1])]
    return g
