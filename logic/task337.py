def p(g):
 for r in g:
  for i,v in enumerate(r):
   if v in (5,8):r[i]=13-v
 return g
