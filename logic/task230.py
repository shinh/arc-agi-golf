def p(g):
 o=[r[:]for r in g]
 h=len(g);w=len(g[0])
 for y in range(h-1):
  for x in range(w-1):
   if g[y][x]==g[y][x+1]==g[y+1][x]==g[y+1][x+1]==5:
    for dy,dx,v in(-1,-1,1),(-1,2,2),(2,-1,3),(2,2,4):
     Y=y+dy;X=x+dx
     if 0<=Y<h and 0<=X<w:o[Y][X]=v
 return o
