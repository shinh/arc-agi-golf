def p(g):
 m=len(g[0])
 for i in range(2,len(g)):g[i]=[g[0][(i-2)%m]]*m
 return g
