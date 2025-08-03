def p(g):
 t=[r[:]for r in g]
 for y in range(9):
  for x in range(9):
   v=t[y][x]
   if v and v<3:
    for Y,X in (((1,0),(-1,0),(0,1),(0,-1)),((1,1),(1,-1),(-1,1),(-1,-1)))[v-1]:
     Y+=y;X+=x
     if -1<Y<9 and -1<X<9:g[Y][X]=(7,4)[v-1]
 return g
