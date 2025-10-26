def p(g,s=1):
 for _ in 0,0,0,0:
  g=[*map(list,zip(*g[::-1]))];t,u=g[0],g[-1]
  if s*(2 in t+u):
   for r in range(len(g)):
    if g[r][0]>7:
     o=0
     for c in range(len(t)):
      o+=(t[c]==2)-(u[c]==2)
      if 0<=r+o<len(g):g[r+o][c]=8
     s=0
 return g