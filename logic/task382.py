def p(g,s=1):
 for _ in[0]*4:
  g=[*map(list,zip(*g[::-1]))];t,u=g[0],g[-1]
  if s*(2 in t+u):
   for r,R in enumerate(g):
    if R[0]>7:
     for c,a in enumerate(t):
      r+=(a==2)-(u[c]==2)
      if-1<r<len(g):g[r][c]=8
     s=0
 return g