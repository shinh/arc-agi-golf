def p(g):# flood fill shapes, count patterns, recolor odd one
 m={}
 for k in range(100):
  i,j=divmod(k,10)
  if g[i][j]:
   o=[(i,j)];g[i][j]=0
   for x,y in o:
    for d in(-1,0,1):
     for e in(-1,0,1):
      u,v=x+d,y+e
      if d|e and 0<=u<10>v>=0 and g[u][v]:g[u][v]=0;o+=[(u,v)]
   s=frozenset((x-min(x for x,_ in o),y-min(y for _,y in o))for x,y in o)
   m[s]=m.get(s,[])+[o]
 t=min(m,key=lambda k:len(m[k]))
 for k in m:
  c=1+(k==t)
  for o in m[k]:
   for i,j in o:g[i][j]=c
   c=1
 return g
