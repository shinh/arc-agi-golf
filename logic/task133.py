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
 t=[divmod(z,w)for z in t];y,x=min((i,j)for i,j in t if G[i][j]==k);t=[(i-y,j-x,G[i][j]==k)for i,j in t]
 for e in o:
  m=[divmod(z,w)for z in e if -g[z]==k];Y,X=map(min,zip(*m));n=max(j for _,j in m)+1-X;c=next(-g[z]for z in e if -g[z]-k)
  for i,j,v in t:
   for a in range(n*n):G[i*n+a//n+Y][j*n+a%n+X]=[c,k][v]
 return G

