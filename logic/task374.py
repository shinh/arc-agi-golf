def p(g):# recursive flood fill
 H=len(g);W=len(g[0])
 def f(y,x):
  if-1<y<H and-1<x<W and g[y][x]==5:
   g[y][x]=0
   return[(y,x)]+f(y+1,x)+f(y-1,x)+f(y,x+1)+f(y,x-1)
  return[]
 for s,w in zip(sorted((f(y,x)for y in range(H)for x in range(W)if g[y][x]==5),key=len),(2,4,1)):
  for y,x in s:g[y][x]=w
 return g
