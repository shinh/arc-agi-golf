def p(g):
 h=w=10;v=set()
 for i in range(h):
  for j in range(w):
   if g[i][j]==5 and (i,j) not in v:
    q=[(i,j)];c=[]
    while q:
     x,y=q.pop()
     if (x,y)in v:continue
     v.add((x,y));c.append((x,y))
     for dx,dy in((1,0),(-1,0),(0,1),(0,-1)):
      nx,ny=x+dx,y+dy
      if 0<=nx<h and 0<=ny<w and g[nx][ny]==5 and (nx,ny)not in v:q.append((nx,ny))
    t=2 if len(c)==6 else 1
    for x,y in c:g[x][y]=t
 return g
