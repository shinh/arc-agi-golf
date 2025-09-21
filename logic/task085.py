# 146 zero tile when identical
def p(g):
 for r,a,b in zip(g,g[-1:]+g,g[1:]+g):
  for x,v in enumerate(r):r[x]-=(v==a[x]==b[x])*(r[x-1:x+2]==[v]*3)*v
 return g
