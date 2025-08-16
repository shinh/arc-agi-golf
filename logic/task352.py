def p(g):
 # expand 1s around 2s
 for y,r in enumerate(g):
  for x,v in enumerate(r):
   if v==2:
    for Y in y-1,y,y+1:
     for X in x-1,x,x+1:
      if -1<Y<len(g) and -1<X<len(r) and g[Y][X]<1:g[Y][X]=1
 return g

