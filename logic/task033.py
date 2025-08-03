def p(g):
 c=g[5][0];a=[(y,x)for y in range(1,4)for x in range(1,4)if g[y][x]]
 for Y in range(3):
  for X in range(3):
   for y,x in a:
    i=Y*6+y;j=X*6+x
    if g[i][j]<1:g[i][j]=c
 return g
