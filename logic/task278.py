# surround 2-pairs with 3
def p(g):
 for _ in 0,1:
  for y,r in enumerate(g):
   for x in range(len(r)):
    if r[x:x+2]==[2]*2:
     for Y in range(y-1,y+2):
      for X in range(x-1,x+3):
       if len(g)>Y>=0<=X<len(r)and g[Y][X]-2:g[Y][X]=3
  g=[*map(list,zip(*g))]
 return g

