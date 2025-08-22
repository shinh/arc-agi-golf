#paint8snear6
def p(g):
 for y in range(15):
  for x in range(15):
   if g[y][x]==6:
    Y,X=y,x
    while g[Y][x]==6:Y+=1
    while g[y][X]==6:X+=1
    for i in range(y-1,Y+1):
     for j in range(x-1,X+1):
      if g[i][j]>7:g[i][j]=3+(y<i<Y)*(x<j<X)
 return g
