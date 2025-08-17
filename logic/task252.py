def p(g):
 # use first row/col to draw diagonals
 r=range(len(g))
 for x in r[1::2]:
  for y in r[x:]:
   if g[0][y-x]:g[x][y]=4
   if g[y-x][0]:g[y][x]=4
 return g
