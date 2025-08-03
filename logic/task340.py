def p(g):
 m=len(g);n=len(g[0]);o=[r[:] for r in g]
 for y in range(1,m-1):
  for x in range(1,n-1):o[y][x]=0
 t,b,l,r=g[0][1],g[-1][1],g[1][0],g[1][-1]
 for y in range(1,m-1):
  for x in range(1,n-1):
   v=g[y][x]
   if v==l:o[y][1]=v
   if v==r:o[y][-2]=v
   if v==t:o[1][x]=v
   if v==b:o[-2][x]=v
 return o
