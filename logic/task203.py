def p(g,r=range,i=0):# fill concentric frames using reversed diagonal
    n=len(g)
    for c in[g[i][i]for i in r(n//2)][::-1]:
        for j in r(i,n-i):g[i][j]=g[~i][j]=g[j][i]=g[j][~i]=c
        i+=1
    return g
