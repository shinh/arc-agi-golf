def p(g):
 n=len(g);s=[[0]*n for _ in g];B={}
 for i in range(n):
  for j in range(n):
   if s[i][j]:continue
   c=g[i][j];t=[(i,j)];s[i][j]=1;C=[];r0=r1=i;c0=c1=j
   while t:
    x,y=t.pop();C.append((x,y));r0=min(r0,x);r1=max(r1,x);c0=min(c0,y);c1=max(c1,y)
    for u,v in((1,0),(0,1),(-1,0),(0,-1)):
     nx,ny=x+u,y+v
     if 0<=nx<n and 0<=ny<n and not s[nx][ny] and g[nx][ny]==c:s[nx][ny]=1;t.append((nx,ny))
   if r1>r0+1 and c1>c0+1 and len(C)==2*(r1-r0+c1-c0)and all(x in(r0,r1)or y in(c0,c1)for x,y in C):B.setdefault(c,[]).append((r0,c0,r1,c1))
 C=min(B,key=lambda k:(len(B[k]),k));r0,c0,r1,c1=B[C][0];h=r1-r0+1;w=c1-c0+1;iH=h-2;iW=w-2;R=[(x,y)for x in range(h)for y in range(w)if x in(0,h-1)or y in(0,w-1)];o=[r[:]for r in g]
 for i in range(n-iH+1):
  for j in range(n-iW+1):
   if all(g[i+x][j+y]==0 for x in range(iH)for y in range(iW)if x in(0,iH-1)or y in(0,iW-1)):
    for x,y in R:
     a=i-1+x;b=j-1+y
     if 0<=a<n and 0<=b<n:o[a][b]=C
 return o
