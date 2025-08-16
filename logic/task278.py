# surround 2-pairs with 3
def p(g):
 for _ in 0,1:
  for y,r in enumerate(g):
   for x in range(len(r)-1):
    if r[x]==r[x+1]==2:
     for Y in range(y-1,y+2):
      for X in range(x-1,x+3):
       if 0<=Y<len(g)and 0<=X<len(r)and g[Y][X]!=2:g[Y][X]=3
  g=[*map(list,zip(*g))]
 return g

