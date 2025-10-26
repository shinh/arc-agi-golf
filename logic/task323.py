def p(g):
 k=sum(g,[]).index(8)#spir
 for d in-1,1:
  r,c=k//13,k%13
  for t in range(169):
   r+=d*(t%4<2);c-=d*(t%4>1)
   if-1<r<13>c>-1:g[r][c]=5
 return g