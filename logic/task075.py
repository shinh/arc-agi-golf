def p(g):
 # stamp top-left 3x3 block around each 1
 b=g[:3]
 for y,r in enumerate(g):
  for x,v in enumerate(r):
   if v==1:
    for dy in 0,1,2:g[y+dy-1][x-1:x+2]=b[dy][:3]
 return g

