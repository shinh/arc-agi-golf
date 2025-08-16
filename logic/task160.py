def p(g):
 r=range(8)# ring->cross
 for y in r:
  a,b,c=g[y:y+3]
  for x in r:
   if b[x+1]<1<sum(sum(r[x:x+3])for r in(a,b,c))>7:
    a[x:x+3]=c[x:x+3]=0,2,0;b[x:x+3]=2,2,2
 return g
