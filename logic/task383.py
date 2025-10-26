def p(g):
 #extend edge lines
 r=range;h=len(g);w=len(g[0])
 Y,X=zip(*[(y,x)for y in r(h)for x in r(w)if g[y][x]])
 y0=Y[0];y1=Y[-1];x0=min(X);x1=max(X)
 a,b=g[y0+2][x0+2],g[y0][x0]
 for x in r(w):
  if a in(g[y0][x],g[y0+1][x],g[y1-1][x],g[y1][x]):
   for y in r(h):g[y][x]=(a,b)[y0<=y<=y1]
 for y in r(h):
  if a in(g[y][x0],g[y][x0+1],g[y][x1-1],g[y][x1]):
   for x in r(w):g[y][x]=(a,b)[x0<=x<=x1]
 return g

