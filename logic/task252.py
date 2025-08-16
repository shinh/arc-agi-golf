def p(g):
 # use first row/col to draw diagonals
 for x in range(1,len(g),2):
  for y in range(x,len(g)):
   if g[0][y-x]:g[x][y]=4
   if g[y-x][0]:g[y][x]=4
 return g
