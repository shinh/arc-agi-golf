def p(g):
 r=range;h=len(g);w=len(g[0])
 nz=[(y,x) for y in r(h) for x in r(w) if g[y][x]]
 y0=min(y for y,_ in nz);y1=max(y for y,_ in nz);x0=min(x for _,x in nz);x1=max(x for _,x in nz)
 a=g[y0+2][x0+2];b=next(g[y][x] for y,x in nz if g[y][x]-a)
 C=[x for x in r(x0,x1+1) if g[y0][x]==a or g[y0+1][x]==a or g[y1-1][x]==a or g[y1][x]==a]
 Y=[y for y in r(y0,y1+1) if g[y][x0]==a or g[y][x0+1]==a or g[y][x1-1]==a or g[y][x1]==a]
 for x in C:
  for y in r(h): g[y][x]=(b,a)[y<y0 or y>y1]
 for y in Y:
  for x in r(w): g[y][x]=(b,a)[x<x0 or x>x1]
 return g

