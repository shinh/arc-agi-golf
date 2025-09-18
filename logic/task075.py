def p(g):
 # copy TL 3x3 to 1s
 for y,r in enumerate(g):
  for x,v in enumerate(r):
   for dy in(0,1,2)*(v==1):g[y+dy-1][x-1:x+2]=g[dy][:3]
 return g
