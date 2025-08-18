def p(g):
 # expand 3x3 complement blocks then color outer ring by parity
 h=len(g);w=len(g[0]);o=[[0]*w for _ in g];a=h;b=0;c=w;d=0;u=sum({*sum(g,[])})
 for y,r in enumerate(g):
  for x,k in enumerate(r):
   if k:
    a=min(a,y);b=max(b,y);c=min(c,x);d=max(d,x);v=u-k
    for i in range(y-1,y+2):
     for j in range(x-1,x+2):
      if h>i>=0<=j<w:o[i][j]=v
    o[y][x]=k
 for i in a,b:
  for j in range(c,d+1):
   if o[i][j]<1 and min(j-c,d-j)%2<1:o[i][j]=5
 for j in c,d:
  for i in range(a,b+1):
   if o[i][j]<1 and min(i-a,b-i)%2<1:o[i][j]=5
 return o

