def p(g):
 h=len(g);w=len(g[0])
 for y in range(h-1):
  for x in range(w-1):
   if g[y][x]==g[y+1][x]==g[y][x+1]==g[y+1][x+1]==0:
    W=2
    while x+W<w and g[y][x+W]==g[y+1][x+W]==0:W+=1
    H=2
    while y+H<h and all(g[y+H][xx]==0 for xx in range(x,x+W)):H+=1
    for Y in range(y,y+H):
     for X in range(x,x+W):g[Y][X]=2
 return g
