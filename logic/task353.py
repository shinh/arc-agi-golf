def p(g):
 for y,r in enumerate(g):
  for x,v in enumerate(r):
   if v==3:sY,sX=y,x
   if v==4:tY,tX=y,x
 g[sY][sX]=0
 g[sY+(tY>sY)-(tY<sY)][sX+(tX>sX)-(tX<sX)]=3
 return g

