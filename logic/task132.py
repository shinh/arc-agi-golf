def p(g):
 # fill each color's bounding box
 e=enumerate
 for k in{*sum(g,[])}-{0}:
  y,x=zip(*((i,j)for i,r in e(g)for j,v in e(r)if v==k))
  a=min(x);b=-~max(x)
  for r in g[min(y):-~max(y)]:r[a:b]=[k]*(b-a)
 return g
