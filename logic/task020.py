# mirror around axes
def p(g):
 a,b=[bytes(map(any,x)).find(1)+2for x in(g,zip(*g))]
 c=-a
 for r in g:
  d=-b
  for v in r:
   if v:g[a+c][b-d]=g[a-c][b-d]=g[a-d][b+c]=g[a+d][b-c]=v
   d+=1
  c+=1
 return g
