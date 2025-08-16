# extend lines from 2 toward 8, painting around the 8
def p(g):
 h=len(g);w=len(g[0])
 for y,x in[(i//w,i%w)for i in range(h*w)if g[i//w][i%w]==2]:
  for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
   ny=y+dy;nx=x+dx;d=0
   while h>ny>=0<w>nx>=0 and g[ny][nx]<1:ny+=dy;nx+=dx;d+=1
   if h>ny>=0<w>nx>=0 and g[ny][nx]==8:
    for i in range(1,d+1):g[y+dy*i][x+dx*i]=2
    for Y in range(ny-1,ny+2):
     for X in range(nx-1,nx+2):
      if h>Y>=0<w>X>=0:g[Y][X]=8
    g[ny][nx]=2
 return g
