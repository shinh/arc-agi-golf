def p(g):
 R=range;m=min;M=max;E=enumerate;g=[r[:]for r in g];h=len(g);w=len(g[0])
 q=[(i,j)for i in R(h)for j in R(w)if not g[i][j]and(i in(0,h-1)or j in(0,w-1))];v=set(q)
 for x,y in q:
  for X,Y in((1,0),(-1,0),(0,1),(0,-1)):
   a,b=x+X,y+Y
   if 0<=a<h and 0<=b<w and not g[a][b]and(a,b)not in v:v.add((a,b));q+=[(a,b)]
 u=[(i,j)for i in R(h)for j in R(w)if not g[i][j]and(i,j)not in v]
 x,y=zip(*u);a=m(x)-1;b=m(y)-1;d=M(x)+2;e=M(y)+2
 G=[r[b:e]for r in g[a:d]];T=[r[1:-1]for r in G[1:-1]]
 k=m({x for r in T for x in r},key=lambda x:x==0)
 I={(i+1,j+1)for i,r in E(T)for j,x in E(r)if x==k}
 B={(i,j)for i,r in E(G)for j,x in E(r)if x==k}-I
 for a in I:
  for b in B:
   if a[0]==b[0]:
    for j in R(m(a[1],b[1]),M(a[1],b[1])+1):G[a[0]][j]=k
   if a[1]==b[1]:
    for i in R(m(a[0],b[0]),M(a[0],b[0])+1):G[i][a[1]]=k
 return G
