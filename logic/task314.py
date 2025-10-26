def p(g):
 for i in 0,1,3,4,6,7:
  for j in 0,1:
   if g[i][j]==g[i][j+6]!=1:g[i][j+3]=g[i][j]
   if g[j][i]==g[j+6][i]!=1:g[j+3][i]=g[j][i]
 return g