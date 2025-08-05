def p(g):
 L,T,R,B=[99]*10,[99]*10,[0]*10,[0]*10
 for y,r in enumerate(g):
  for x,v in enumerate(r):
   if x<L[v]:L[v]=x
   if y<T[v]:T[v]=y
   if x>R[v]:R[v]=x
   if y>B[v]:B[v]=y
 f=a=0
 for v in range(1,10):
  if L[v]<99:
   l,r,t,u=L[v],R[v],T[v],B[v]
   A=(r-l+1)*(u-t+1)
   if all((g[y][x]==v)==(x==l or x==r or y==t or y==u)for y in range(t,u+1)for x in range(l,r+1))and A>a:f=v;a=A
 px=py=99;qx=qy=0
 for v in range(1,10):
  if v-f:
   if L[v]<px:px=L[v]
   if T[v]<py:py=T[v]
   if R[v]>qx:qx=R[v]
   if B[v]>qy:qy=B[v]
 fw=R[f]-L[f]+1;fh=B[f]-T[f]+1
 kx=(fw-2)//(qx-px+1);ky=(fh-2)//(qy-py+1)
 o=[[f]*fw]+[[f]+[0]*(fw-2)+[f] for _ in range(fh-2)]+[[f]*fw]
 for y in range(fh-2):
  for x in range(fw-2):
   v=g[py+y//ky][px+x//kx]
   if v and v-f:o[1+y][1+x]=v
 return o
