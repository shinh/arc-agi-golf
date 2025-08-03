def p(g):
 n=len(g)
 for i in range(n):g[i][i]=g[i][~i]=0
 return g
