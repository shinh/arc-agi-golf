def p(g,m=-1):
 for r in g[::-1]:
  p,m,o=m,-1,[0]*len(r)
  for x,v in enumerate(r):
   if v:m=x;o[x+(p>x)]=v
  r[:]=o
 return g
