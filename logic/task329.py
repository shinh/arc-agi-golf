def p(g):
 m=len(g[0])//2
 for r in g:r[:]=[0]*m+[r[m]]+[0]*m
 return g
