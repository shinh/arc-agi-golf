def p(g):
 h=[r[:]for r in g];k=max(v for r in g for v in r if v!=2)
 for y in range(9):
  for x in range(9):
   if g[y][x]==2:
    a=b=0
    for i,j in(-1,0),(1,0),(0,-1),(0,1):
     if 0<=y+i<9 and 0<=x+j<9 and g[y+i][x+j]==k:a-=i;b-=j
    Y,X=y,x
    while-1<Y<9 and-2<X<10:
     for j in-1,0,1:
      u=X+j
      if 0<=u<9 and 0<=Y<9:h[Y][u]=k
     Y+=a;X+=b
 return h
