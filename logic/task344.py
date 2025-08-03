def p(g):
 h=len(g);w=len(g[0]);o=[r[:] for r in g]
 for y in range(h):
  for x in range(w):
   v=g[y][x]
   if v==3 and ((y and g[y-1][x]==2)or(y<h-1 and g[y+1][x]==2)or(x and g[y][x-1]==2)or(x<w-1 and g[y][x+1]==2)):o[y][x]=8
   if v==2 and ((y and g[y-1][x]==3)or(y<h-1 and g[y+1][x]==3)or(x and g[y][x-1]==3)or(x<w-1 and g[y][x+1]==3)):o[y][x]=0
 return o
