def p(g):# recolor rectangular loops
 R=range;h=len(g);w=len(g[0])
 for y in R(h):
  for x in R(w):
   if g[y][x]>0:
    X=x;Y=y
    while X<w and g[y][X]>0:X+=1
    while Y<h and g[Y][x]>0:Y+=1
    if X-x>1<Y-y and all(g[Y-1][i]>0 for i in R(x,X))and all(g[i][X-1]>0 for i in R(y,Y))and any(0in g[i][x:X]for i in R(y,Y)):
     for i in R(x,X):g[y][i]=g[Y-1][i]=3
     for i in R(y,Y):g[i][x]=g[i][X-1]=3
 return g
