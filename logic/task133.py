def p(G):# flood fill each island then copy scaled pattern of dominant color
 w=len(G[0]);g=sum(G,[]);d=[0]*10;o=[]
 for z,v in enumerate(g):
  if v>0:
   q=[z];g[z]=-v
   for z in q:
    j=z%w
    for n in z-w-1,z-w,z-w+1,z-1,z+1,z+w-1,z+w,z+w+1:
     if 0<=n<len(g) and -2<n%w-j<2 and 0<g[n]:g[n]=-g[n];q+=n,
   for a in{-g[u]for u in q}:d[a]+=1;o+=q,
 k=d.index(max(d));t=min(o,key=lambda e:(sum(-g[u]==k for u in e),-len(e)));o.remove(t)
 Y,X=map(min,zip(*(t:=[divmod(z,w)for z in t])))
 t=[(i-Y,j-X,G[i][j]==k)for i,j in t];y,x=min((i,j)for i,j,v in t if v)
 for e in o:
  Y,X=map(min,zip(*(m:=[divmod(z,w)for z in e if -g[z]==k])));n=max(j for _,j in m)+1-X;c=next(-g[z]for z in e if -g[z]!=k)
  for i,j,v in t:
   for a in range(n*n):G[i*n+a//n+Y-y*n][j*n+a%n+X-x*n]=[c,k][v]
 return G

