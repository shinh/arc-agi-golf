def p(g):
 m=-1
 for r in g[::-1]:
  o=[0]*len(r);n=-1
  for x,v in enumerate(r):
   if v:n=x;o[x+(m>x)]=v
  r[:]=o;m=n
 return g