def p(g,r=range,i=0):
    n=len(g);L=[g[i][i] for i in r(n//2)][::-1]
    for c in L:
        for x in r(i,n-i):g[i][x]=g[~i][x]=c
        for y in r(i,n-i):g[y][i]=g[y][~i]=c
        i+=1
    return g
