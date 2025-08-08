def p(g):
 R=range;m=min;M=max;E=enumerate;g=[r for r in g];h=len(g);w=len(g[0])
 f=lambda x,y:0<=x<h and 0<=y<w and not g[x][y]and not g[x].__setitem__(y,1)and[f(x+1,y),f(x-1,y),f(x,y+1),f(x,y-1)]
 for i in R(h):f(i,0);f(i,w-1)
 for j in R(w):f(0,j);f(h-1,j)
 x,y=zip(*[(i,j)for i in R(h)for j in R(w)if not g[i][j]]);a=m(x)-1;b=m(y)-1;d=M(x)+2;e=M(y)+2
 G=[r[b:e]for r in g[a:d]];T=[r[1:-1]for r in G[1:-1]]
 k=m(({*sum(T,[])}-{0})or{0})
 I={(i+1,j+1)for i,r in E(T)for j,x in E(r)if x==k}
 B={(i,j)for i,r in E(G)for j,x in E(r)if x==k}-I
 for i,j in I:
  for x,y in B:
   if i==x:
    for t in R(m(j,y),M(j,y)+1):G[i][t]=k
   if j==y:
    for t in R(m(i,x),M(i,x)+1):G[t][j]=k
 return G
