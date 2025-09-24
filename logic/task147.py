# recolor any 3 touching another 3 to 8
def p(g):
 for n in(s:={y*64+x for y,r in enumerate(g)for x,v in enumerate(r)if v==3}):
  if{n+1,n-1,n+64,n-64}&s:g[n>>6][n&63]=8
 return g

