def p(g):
 h=len(g);w=len(g[0]);r=[r[:]for r in g]
 for i in range(h):
  for j in range(w):
   c=g[i][j]
   if c and c!=3:
    for dx,dy in((1,0),(-1,0),(0,1),(0,-1)):
     x,y=i+dx,j+dy
     while 0<=x<h and 0<=y<w and g[x][y]==0:x+=dx;y+=dy
     if 0<=x<h and 0<=y<w and g[x][y]==3:
      x-=dx;y-=dy
      while(x,y)!=(i,j):r[x][y]=c;x-=dx;y-=dy
 return r
