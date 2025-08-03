def p(g):
 for r in g:
  for i in range(1,len(r)-1):
   if r[i]==0<r[i-1]==r[i+1]==1:r[i]=2
 return g
