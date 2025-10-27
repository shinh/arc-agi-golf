def p(g,m=-1):
 for r in g[::-1]:
  p,m=m,-1
  for x,v in enumerate(r):v and(m:=x)
  r[:0]=0,;r[p]=r.pop(p+1)or r[p]
 return g
