def p(g):
 R=[-1]+[i for i,r in enumerate(g)if max(r)<1]
 C=[-1]+[i for i,c in enumerate(zip(*g))if max(c)<1]
 return[[max(g[i+1][j+1:j+4]+g[i+3][j+1:j+4])for j in C]for i in R]
