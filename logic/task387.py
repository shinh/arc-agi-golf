def p(g):
 # flood fill each color, draw complement borders, then color outer ring by parity
 h=len(g);w=len(g[0]);o=[r[:]for r in g];f=[];a=h;c=w;b=d=0;u=sum({*sum(g,[])})
 for y in range(h):
  for x in range(w):
   if k:=g[y][x]:
    g[y][x]=0;q=[(y,x)];A=B=y;C=D=x
    for i,j in q:
     f+=[(i,j)];a=min(a,i);b=max(b,i);c=min(c,j);d=max(d,j);A=min(A,i);B=max(B,i);C=min(C,j);D=max(D,j)
     for I,J in(i+1,j),(i-1,j),(i,j+1),(i,j-1):
      if h>I>=0<=J<w and g[I][J]==k:g[I][J]=0;q+=[(I,J)]
    k=u-k;A-=A>0;B+=h-1>B;C-=C>0;D+=w-1>D
    for j in range(C,D+1):o[A][j]=o[B][j]=k
    for i in range(A,B+1):o[i][C]=o[i][D]=k
 for i in range(a,b+1):
  for j in range(c,d+1):
   if(i in(a,b)or j in(c,d))and o[i][j]<1 and min(abs(i-y)+abs(j-x)for y,x in f)&1<1:o[i][j]=5
 return o
