def p(g):
 a,b=[bytes(map(any,x)).find(1)+2for x in(g,zip(*g))]
 for c,r in enumerate(g,-a):
  for d,v in enumerate(r,-b):
   if v:g[a+c][b-d]=g[a-c][b-d]=g[a-d][b+c]=g[a+d][b-c]=v
 return g
