def p(g):
 for u,r,d in zip(g,g[1:],g[2:]):
  for a,b in zip(t:=(i for i in range(12)if u[i]*r[i]*d[i]),t):r[a+1:b]=[(i:=b+~a)+5]*i
 return g