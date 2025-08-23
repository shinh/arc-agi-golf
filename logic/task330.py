def p(g):# flood fill groups of 5; size 6->2 else 1
 def f(x,y):
  if-1<x<10>y>-1<g[x][y]==5:
   g[x][y]=0
   return[(x,y)]+f(x+1,y)+f(x-1,y)+f(x,y+1)+f(x,y-1)
  return[]
 for i in range(100):
  if c:=f(*divmod(i,10)):
   for x,y in c:g[x][y]=1+(len(c)==6)
 return g
