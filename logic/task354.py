def p(g):
 t=g[0][:];h=len(g);w=len(g[0])
 for y in range(h):
  for x in range(w):
   if g[y][x]==5:
    q=[(y,x)];g[y][x]=0;c=0
    for i,j in q:
     if t[j]:c=t[j]
     for a,b in(1,0),(-1,0),(0,1),(0,-1):
      u=i+a;v=j+b
      if 0<=u<h and 0<=v<w and g[u][v]==5:g[u][v]=0;q.append((u,v))
    for i,j in q:g[i][j]=c
 return g

