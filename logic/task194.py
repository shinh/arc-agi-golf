def p(g):
 n=len(g)
 o=[[0]*n*2 for _ in g*2]
 for y in range(n):
  for x in range(n):
   v=g[y][x]
   o[y][x]=v
   o[x][2*n-1-y]=v
   o[2*n-1-x][y]=v
   o[2*n-1-y][2*n-1-x]=v
 return o
