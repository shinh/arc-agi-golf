def p(g):
 h=[r[:]for r in g];m=0,
 #show(g,"in")
 for z in range(400):
  y,x=divmod(z,20)
  if g[y][x]:
   q=[(y,x)];g[y][x]=0;y0=y1=y;x0=x1=x;c=h[y][x]>1
   while q:
    y,x=q.pop()
    for a,b in((y+1,x),(y-1,x),(y,x+1),(y,x-1)):
     if 20>a>=0<=b<20 and g[a][b]:q.append((a,b));g[a][b]=0;c+=h[a][b]>1;y0=min(y0,a);y1=max(y1,a);x0=min(x0,b);x1=max(x1,b)
   b=[r[x0:x1+1]for r in h[y0:y1+1]];k=c,len(b),len(b[0])
   if k>m:m=k;o=b
 #show(o,"out")
 return o
