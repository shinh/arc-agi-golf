def p(g):
 h=len(g);w=len(g[0]);o=[r for r in g]
 for y in range(h):
  for x in range(w):
   c=g[y][x]
   if c and all(0>y+dy or y+dy>=h or 0>x+dx or x+dx>=w or g[y+dy][x+dx]!=c for dy in(-1,0,1) for dx in(-1,0,1) if dy or dx):
    o[y][x]=0
 return o
