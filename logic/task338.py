# Just solved.
#
# Based on 029
# fill holes
def p(g):
 s=[0,0,-1,0]
 while s:
  try:
   y=s.pop();x=s.pop()
   if g[y][x]<2:g[y][x]=4;s+=x,y+1,x,y-1,x+1,y,x-1,y
  except:0
 for r in g:r[:]=[3*(v<1)for v in r]
 return g
