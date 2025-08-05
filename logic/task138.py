def p(g):
 g=[r[:]for r in g];h=len(g);w=len(g[0])
 v=set();u=[]
 for i in range(h):
  for j in range(w):
   if not g[i][j] and(i,j)not in v:
    q=[(i,j)];s=[];b=0;v.add((i,j))
    while q:
     x,y=q.pop();s+=[(x,y)];b|=x in(0,h-1)or y in(0,w-1)
     for dx,dy in((1,0),(-1,0),(0,1),(0,-1)):
      nx,ny=x+dx,y+dy
      if 0<=nx<h and 0<=ny<w and not g[nx][ny] and(nx,ny)not in v:v.add((nx,ny));q+=[(nx,ny)]
    if not b:u+=s
 a=min(i for i,_ in u)-1;b=min(j for _,j in u)-1
 d=max(i for i,_ in u)+2;e=max(j for _,j in u)+2
 G=[r[b:e]for r in g[a:d]];T=[r[1:-1]for r in G[1:-1]]
 k=min({x for r in T for x in r},key=lambda x:x==0)
 I={(i+1,j+1)for i,r in enumerate(T)for j,x in enumerate(r)if x==k}
 B={(i,j)for i,r in enumerate(G)for j,x in enumerate(r)if x==k}-I
 for a in I:
  for b in B:
   if a[0]==b[0]:
    for j in range(min(a[1],b[1]),max(a[1],b[1])+1):G[a[0]][j]=k
   elif a[1]==b[1]:
    for i in range(min(a[0],b[0]),max(a[0],b[0])+1):G[i][a[1]]=k
 return G
