def p(g):
 c=0;h=len(g);w=len(g[0])
 for y in range(h):
  for x in range(w):
   if g[y][x]==8:
    c+=1;g[y][x]=0;q=[(y,x)]
    while q:
     Y,X=q.pop()
     for dY,dX in((1,0),(-1,0),(0,1),(0,-1)):
      nY=Y+dY;nX=X+dX
      if 0<=nY<h and 0<=nX<w and g[nY][nX]==8:
       g[nY][nX]=0;q+=[(nY,nX)]
 o=create(c,c)
 for i in range(c):o[i][i]=8
 return o
