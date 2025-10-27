def p(g):
 for d in-1,1:
  r,c=divmod(sum(g,[]).index(8),13)#s
  for t in range(169):
   b=t&2>0;r+=d-d*b;c-=d*b
   if-1<r<13>c>-1:g[r][c]=5
 return g