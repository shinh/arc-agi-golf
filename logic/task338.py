# Just solved.
#
# Based on 029
# fill holes
def p(g):
 def f(x,y):
  try:
   if g[y][x]<2:g[y][x]=4;f(x,y+1);f(x,y-1);f(x+1,y);f(x-1,y)
  except:0
 f(0,0);f(0,-1)
 return[[3*(v<1)for v in r]for r in g]
