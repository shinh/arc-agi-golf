def p(g):
 # shift interior colors to inner edges
 m=len(g);t,b,l,r=g[0][1],g[-1][1],g[1][0],g[1][-1];R=range
 for y in R(1,m-1):
  k=g[y]
  for x in R(1,len(k)-1):
   v=k[x];k[x]=0
   if v==l:k[1]=v
   if v==r:k[-2]=v
   if v==t:g[1][x]=v
   if v==b:g[-2][x]=v
 return g
