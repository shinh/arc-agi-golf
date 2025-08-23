# extend lines from 2 toward 8, painting around the 8
def p(g):
 h=len(g);w=len(g[0])
 for y,x in[(y,x)for y in range(h)for x in range(w)if g[y][x]==2]:
  for dy,dx in(1,0),(-1,0),(0,1),(0,-1):
   ny=y+dy;nx=x+dx;d=0
   while h>ny>=0<w>nx>=0 and g[ny][nx]<1:ny+=dy;nx+=dx;d+=1
   if h>ny>=0<w>nx>=0 and g[ny][nx]==8:
    while d:g[y+dy*d][x+dx*d]=2;d-=1
    for Y in ny-1,ny,ny+1:
     for X in nx-1,nx,nx+1:
      if h>Y>=0<w>X>=0:g[Y][X]=8
    g[ny][nx]=2
 return g
