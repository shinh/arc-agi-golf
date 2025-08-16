def p(g):
 # flood-fill rectangles framed by 1's with inner color
 v=[[0]*10 for _ in g]
 for y in range(10):
  for x in range(10):
   if g[y][x]==1 and not v[y][x]:
    q=[(y,x)];v[y][x]=1;u=d=y;l=r=x
    while q:
     i,j=q.pop()
     for n,m in((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
      if 0<=n<10>m>-1 and g[n][m]==1 and not v[n][m]:
       v[n][m]=1;q+=[(n,m)];u=min(u,n);d=max(d,n);l=min(l,m);r=max(r,m)
    c=max(g[i][j]for i in range(u,d+1)for j in range(l,r+1))
    for i in range(u and u-1,d+1):
     for j in range(l,r+1):
      if g[i][j]<1:g[i][j]=c
 return g
