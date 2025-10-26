def p(g):
 R=range;h=len(g)
 l=next(n for n in R(2,h)if len({*g[0][n-1::n]})<2)
 p,q=next((y+l,x+l)for y in R(0,h-l,l)for x in R(0,h-l,l)if(g[y][x]+g[y+l][x]*g[y][x+l])*g[y+l][x+l])
 for y in R(0,h,l):
  for x in R(0,h,l):
   for d in R(-l,2*l-1):
    for e in R(-l,2*l-1):
     if g[y][x]==g[p][q]and-1<y+d<h>x+e>-1:g[y+d][x+e]=g[p+d][q+e]
 return g