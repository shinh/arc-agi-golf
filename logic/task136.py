def p(g):
 a=sum(g,[])
 for v in 1,2:
  r,c=divmod(a.index(v),10);d=2*v-3
  while 0<=r<10>c>=0:g[r][c]=v;r+=d;c+=d
 return g