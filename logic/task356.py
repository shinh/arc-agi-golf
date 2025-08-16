def p(g,r=range,E=enumerate):
 # link
 d=[[]for _ in r(10)]
 for y,R in E(g):
  for x,v in E(R):
   if v:
    for Y,X in d[v]:
     if y==Y:
      for u in r(min(x,X),max(x,X)+1):R[u]=v
     elif x==X:
      for u in r(min(y,Y),max(y,Y)+1):g[u][x]=v
    d[v]+=[(y,x)]
 return g

