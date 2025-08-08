def p(g):
 h=len(g);w=len(g[0]);y=-1
 for r in g:
  y+=1;x=-1
  for v in r:
   x+=1
   if v==2:
    for yy in range(y-1,y+2):
     for xx in range(x-1,x+2):
      if 0<=yy<h and 0<=xx<w and g[yy][xx]==0:g[yy][xx]=1
 return g

