def p(g):
 # shift interior colors to inner edges
 u,d=g[1],g[-2]
 for x in range(1,len(u)-1):
  for k in g[1:-1]:
   v,k[x]=k[x],0
   if v==u[0]:k[1]=v
   if v==u[-1]:k[-2]=v
   if v==g[0][1]:u[x]=v
   if v==g[-1][1]:d[x]=v
 return g
