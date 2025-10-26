def p(g):
 i,j=divmod(sum(g,[]).index(8),13)
 for d in-1,1:
  r,c,k=i,j,169
  while k:
   r+=d*(2>k&2);c-=d*(1<k&2);k-=1
   if 13>c>-1<r<13:g[r][c]=5
 return g