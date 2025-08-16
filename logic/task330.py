def p(g):# flood fill groups of 5; size 6->2 else 1
 h=w=10
 def f(x,y):
  if-1<x<h>y>-1 and g[x][y]==5:
   g[x][y]=0
   return[(x,y)]+f(x+1,y)+f(x-1,y)+f(x,y+1)+f(x,y-1)
  return[]
 for i in range(h):
  for j in range(w):
   c=f(i,j)
   if c:
    t=1+(len(c)==6)
    for x,y in c:g[x][y]=t
 return g
