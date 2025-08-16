def p(g):# recolor rectangular loops
 R=range;h=len(g);w=len(g[0])
 for y in R(h):
  for x in R(w):
   if g[y][x]==1:
    X=x
    while X<w and g[y][X]==1:X+=1
    Y=y
    while Y<h and g[Y][x]==1:Y+=1
    if X-x>1<Y-y and all(g[y][i]==g[Y-1][i]==1 for i in R(x,X))and all(g[i][x]==g[i][X-1]==1 for i in R(y,Y))and any(g[i][j]<1 for i in R(y+1,Y-1)for j in R(x+1,X-1)):
     for i in R(x,X):g[y][i]=g[Y-1][i]=3
     for i in R(y,Y):g[i][x]=g[i][X-1]=3
 return g
