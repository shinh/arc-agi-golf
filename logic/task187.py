def p(g):
 h=len(g);w=len(g[0])
 idx=[(0,j)for j in range(w)]+[(h-1,j)for j in range(w)]+[(i,0)for i in range(1,h-1)]+[(i,w-1)for i in range(1,h-1)]
 d={}
 for i,j in idx:
  v=g[i][j];d[v]=d.get(v,0)+1
 c=max(d,key=d.get)
 v=[[0]*w for _ in g];C=[]
 def bfs(sy,sx):
  q=[(sy,sx)];v[sy][sx]=1;cells=[(sy,sx)];b=sy in(0,h-1)or sx in(0,w-1)
  while q:
   y,x=q.pop()
   for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
    ny=y+dy;nx=x+dx
    if 0<=ny<h and 0<=nx<w and not v[ny][nx] and g[ny][nx]==c:
     v[ny][nx]=1;q+=[(ny,nx)];cells+=[(ny,nx)];b|=ny in(0,h-1)or nx in(0,w-1)
  return cells,b
 for i in range(h):
  for j in range(w):
   if not v[i][j] and g[i][j]==c:C+=[bfs(i,j)]
 for cells,b in C:
  if not b:
   for i,j in cells:g[i][j]=2
 for i in range(h):
  for j in range(w):
   if g[i][j]==c:g[i][j]=3
 return g
