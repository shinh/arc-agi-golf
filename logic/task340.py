# shift
def p(g):
 for k in g[1:-1]:
  for x in range(1,len(k)-1):
   v,k[x]=k[x],0
   if v==g[1][0]:k[1]=v
   if v==g[1][0]:k[1]=v
   if v==g[1][0]:k[1]=v
   if v==g[1][-1]:k[-2]=v
   if v==g[1][-1]:k[-2]=v
   if v==g[0][1]:g[1][x]=v
   if v==g[0][1]:g[1][x]=v
   if v==g[-1][1]:g[-2][x]=v
   if v==g[-1][1]:g[-2][x]=v
 return g
