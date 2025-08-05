def p(g):
 h=len(g);w=len(g[0]);o=[r[:]for r in g];t=[];f=[];a=h;b=0;c=w;d=0;u=sum({j for i in g for j in i})
 for y in range(h):
  for x in range(w):
   k=g[y][x]
   if k:
    g[y][x]=0;q=[(y,x)];y0=y1=y;x0=x1=x
    while q:
     i,j=q.pop();f+=[(i,j)];a=min(a,i);b=max(b,i);c=min(c,j);d=max(d,j);y0=min(y0,i);y1=max(y1,i);x0=min(x0,j);x1=max(x1,j)
     for ny,nx in(i+1,j),(i-1,j),(i,j+1),(i,j-1):
      if 0<=ny<h and 0<=nx<w and g[ny][nx]==k:
       g[ny][nx]=0;q+=[(ny,nx)]
    t+=[(u-k,y0,y1,x0,x1)]
 for k,y0,y1,x0,x1 in t:
  y0=max(0,y0-1);y1=min(h-1,y1+1);x0=max(0,x0-1);x1=min(w-1,x1+1)
  for j in range(x0,x1+1):o[y0][j]=o[y1][j]=k
  for i in range(y0,y1+1):o[i][x0]=o[i][x1]=k
 for i in range(a,b+1):
  for j in range(c,d+1):
   if (i in(a,b)or j in(c,d))and o[i][j]<1 and min(abs(i-y)+abs(j-x)for y,x in f)%2<1:o[i][j]=5
 return o
