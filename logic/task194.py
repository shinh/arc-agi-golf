def p(g):
 n=3;o=[[0]*6 for _ in[0]*6]
 for y in range(3):
  for x in range(3):
   v=g[y][x]
   o[y][x]=v
   o[x][5-y]=v
   o[5-x][y]=v
   o[5-y][5-x]=v
 return o
