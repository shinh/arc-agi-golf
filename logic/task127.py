def p(g,q=range):
 for i in q(1,len(g),4):
  for j in q(1,len(g[0]),4):
   v=g[i][j]+5
   for x in q(3):
    for y in q(3):
     g[i-1+x][j-1+y]=v
 return g