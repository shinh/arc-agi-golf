def p(g,r=range,E=enumerate):
 # link
 d=[]
 for y,R in E(g):
  for x,v in E(R):
   if v:
    for Y,X in d:
     if y==Y:
      for u in r(min(x,X),max(x,X)+1):R[u]=8
     elif x==X:
      for u in r(min(y,Y),max(y,Y)+1):g[u][x]=8
    d+=[(y,x)]
 return g

