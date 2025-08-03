def p(g):
 h=len(g);w=len(g[0]);q=[]
 for y in range(h):
  for x in range(w):q+=[(y,x)]*(g[y][x]==1)
 while q:
  y,x=q.pop()
  for Y,X in((y+1,x),(y-1,x),(y,x+1),(y,x-1)):
   if-1<Y<h and-1<X<w and g[Y][X]==0:g[Y][X]=1;q+=[(Y,X)]
 return g
