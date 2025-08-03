def p(g):
 P=[(y,x)for y in range(9)for x in range(9)if g[y][x]==4]
 a=min(y for y,x in P);b=max(y for y,x in P)+1;c=min(x for y,x in P);d=max(x for y,x in P)+1
 o=[]
 for r in g[a:b]:
  t=[]
  for v in r[c:d]:t+=v,v
  o+=t,t
 return o
