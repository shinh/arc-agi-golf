def p(g):
 # flood-fill rectangles framed by 1's with inner color
 for y in range(10):
  for x in range(10):
   if g[y][x]==1:
    q=[(y,x)];g[y][x]=-1;u=d=y;l=r=x
    for i,j in q:
     for n,m in((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
      if 0<=n<10>m>-1 and g[n][m]==1:
       g[n][m]=-1;q+=[(n,m)];u=min(u,n);d=max(d,n);l=min(l,m);r=max(r,m)
    c=max(max(R[l:r+1])for R in g[u:d+1])
    for i in range(u and u-1,d+1):
     R=g[i];R[l:r+1]=[v<0 or v and v or c for v in R[l:r+1]]
 return g

