def p(g):
 r=g[0];m=len(r)
 for i in range(2,len(g)):g[i]=[r[(i-2)%m]]*m
 return g
