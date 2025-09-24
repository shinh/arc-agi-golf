def p(g,r=range):# fill concentric frames using reversed diagonal
    n=len(g);h=[g[i][i]for i in r(n//2)]
    for i in r(n//2):
        for j in r(i,n-i):g[i][j]=g[~i][j]=g[j][i]=g[j][~i]=h[~i]
    return g
