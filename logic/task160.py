def p(g):
 for a,b,c in zip(g,g[1:],g[2:]):#ring->cross
  for x in range(8):
   if b[x+1]<1<sum(a[x:x+3]+b[x:x+3]+c[x:x+3])>7:a[x:x+3]=c[x:x+3]=0,2,0;b[x:x+3]=2,2,2
 return g
