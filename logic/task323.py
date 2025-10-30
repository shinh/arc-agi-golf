def p(g):
 for d in-1,1:
  r,c=divmod(sum(g,[]).index(8),13)#s
  for b in[0,0,1,1]*6:
   r+=d-d*b;c-=d*b
   if-1<r<13>c>-1:g[r][c]=5
 return g