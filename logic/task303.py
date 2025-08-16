def p(g):
 # 0 rows/cols ->2
 for r in g:
  if{*r}=={0}:r[:]=[2]*len(r)
 for x,c in enumerate(zip(*g)):
  if{*c}<={0,2}:
   for r in g:r[x]=2
 return g
