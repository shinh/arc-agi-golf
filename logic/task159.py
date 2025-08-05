def p(g):
 L,T,R,B,C=[99]*10,[99]*10,[0]*10,[0]*10,[0]*10
 for y,r in enumerate(g):
  for x,v in enumerate(r):
   C[v]+=1
   if x<L[v]:L[v]=x
   if y<T[v]:T[v]=y
   if x>R[v]:R[v]=x
   if y>B[v]:B[v]=y
 b=0
 f=lx=rx=ty=by=a=0
 for v in range(10):
  if C[v] and v:
   l,r,t,u=L[v],R[v],T[v],B[v]
   ok=1
   for y in range(t,u+1):
    for x in range(l,r+1):
     if (g[y][x]==v)!=(x==l or x==r or y==t or y==u):ok=0;break
    if not ok:break
   if ok:
    A=(r-l+1)*(u-t+1)
    if A>a:f=v;lx,rx,ty,by=l,r,t,u;a=A
 px=py=99;qx=qy=0
 for v in range(10):
  if C[v] and v and v-f:
   if L[v]<px:px=L[v]
   if T[v]<py:py=T[v]
   if R[v]>qx:qx=R[v]
   if B[v]>qy:qy=B[v]
 fw=rx-lx+1;fh=by-ty+1
 kx=(fw-2)//(qx-px+1);ky=(fh-2)//(qy-py+1)
 o=[[0]*fw for _ in range(fh)]
 for i in range(fw):o[0][i]=o[-1][i]=f
 for i in range(fh):o[i][0]=o[i][-1]=f
 for y in range(py,qy+1):
  for x in range(px,qx+1):
   v=g[y][x]
   if v and v-f:
    for dy in range(ky):
     for dx in range(kx):o[1+(y-py)*ky+dy][1+(x-px)*kx+dx]=v
 return o
