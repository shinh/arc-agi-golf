def p(g):# propagate down
 for x in 0,1,2:
  v=0
  for r in g:r[x]=v=r[x]or v
 return g
