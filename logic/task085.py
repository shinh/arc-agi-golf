# 147
# zero tile when identical to neighbours
def p(g):
 for r,a,b in zip(g,g[-1:]+g,g[1:]+g):
  for x,v in enumerate(r):
   if v==a[x]==b[x]==r[x-1]==(r+[0])[x+1]:r[x]=0
 return g
