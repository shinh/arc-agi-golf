def p(g):
 h,w=len(g),len(g[0])
 s=[(y,x)for y in range(h)for x in range(w)if g[y][x]==2]
 for y,x in s:
  for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
   ny,nx=y,x
   d=0
   while 0<=ny+dy<h and 0<=nx+dx<w and g[ny+dy][nx+dx]==0:
    ny+=dy;nx+=dx;d+=1
   ny+=dy;nx+=dx
   if 0<=ny<h and 0<=nx<w and g[ny][nx]==8:
    for i in range(d):g[y+dy*(i+1)][x+dx*(i+1)]=2
    for Y in range(ny-1,ny+2):
     for X in range(nx-1,nx+2):
      if 0<=Y<h and 0<=X<w:g[Y][X]=8
    g[ny][nx]=2
 return g
