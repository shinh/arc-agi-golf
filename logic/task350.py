def p(g):
 h=len(g);w=len(g[0])
 for r in g:
  l=None
  for x,c in enumerate(r):
   if c==1:
    if l is not None:
     for j in range(l+1,x):r[j]=8
    l=x
 for x in range(w):
  l=None
  for y in range(h):
   if g[y][x]==1:
    if l is not None:
     for i in range(l+1,y):g[i][x]=8
    l=y
 return g

