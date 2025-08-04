def p(g):
 c=g[0][0]
 h=len(g);w=len(g[0])
 out=[[4 if v==c else v for v in r]for r in g]
 seen=set()
 for i in range(h):
  for j in range(w):
   if g[i][j]==c and (i,j)not in seen:
    q=[(i,j)];seen.add((i,j));cells=[]
    while q:
     x,y=q.pop();cells.append((x,y))
     for dx,dy in((1,0),(-1,0),(0,1),(0,-1)):
      nx,ny=x+dx,y+dy
      if 0<=nx<h and 0<=ny<w and g[nx][ny]==c and (nx,ny)not in seen:
       seen.add((nx,ny));q.append((nx,ny))
    if len(cells)>1:
     r0=min(x for x,_ in cells);r1=max(x for x,_ in cells)
     c0=min(y for _,y in cells);c1=max(y for _,y in cells)
     if (r1-r0+1)*(c1-c0+1)==len(cells):
      for x,y in cells:out[x][y]=3
 return out
