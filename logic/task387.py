def p(g):
 # complement bloom parity ring
 h=len(g);w=len(g[0]);o=[[0]*w for _ in g];a=h;b=0;c=w;d=0;u=sum({*sum(g,[])})
 for y,r in enumerate(g):
  for x,k in enumerate(r):
   if k:
    a=min(a,y);b=max(b,y);c=min(c,x);d=max(d,x)
    for i in y-1,y,y+1:
     for j in x-1,x,x+1:
      if h>i>-1<j<w:o[i][j]=u-k
    o[y][x]=k
 for i in a,b:
  for j in range(c,d+1):o[i][j]=o[i][j] or~min(j-c,d-j)&1 and 5
 for j in c,d:
  for i in range(a,b+1):o[i][j]=o[i][j] or~min(i-a,b-i)&1 and 5
 return o

