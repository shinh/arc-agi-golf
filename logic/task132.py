def p(g):
 # fill each color's bounding box
 e=enumerate
 for k in{v for r in g for v in r if v}:
  y,x=zip(*[(i,j)for i,r in e(g)for j,v in e(r)if v==k])
  a=min(x);b=max(x)+1
  for i in range(min(y),max(y)+1):g[i][a:b]=[k]*(b-a)
 return g
