# surround 2-pairs with 3
def p(g):
 for _ in 0,1:
  for y,r in enumerate(g):
   for x in range(len(r)-1):
    if r[x]==r[x+1]==2:
     for Y in range(y-1,y+2):
      for X in range(x-1,x+3):
       if g[Y:Y+1]and g[Y][X:X+1]and g[Y][X]-2:g[Y][X]=3
  g=[*map(list,zip(*g))]
 return g

