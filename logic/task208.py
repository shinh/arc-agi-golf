def p(g):
 n=len(g);B={};o=[r[:]for r in g]
 for i in range(n):
  for j in range(n):
   c=g[i][j]
   if c<1:continue
   t=[(i,j)];C=[];g[i][j]=-1;r0=r1=i;c0=c1=j
   while t:
    x,y=t.pop();C.append(x*n+y);r0=min(r0,x);r1=max(r1,x);c0=min(c0,y);c1=max(c1,y)
    for u,v in((1,0),(0,1),(-1,0),(0,-1)):
     nx,ny=x+u,y+v
     if n>nx>=0<=ny<n and g[nx][ny]==c:g[nx][ny]=-1;t.append((nx,ny))
   if r1>r0+1 and c1>c0+1 and len(C)==2*(r1-r0+c1-c0)and all(p//n in(r0,r1)or p%n in(c0,c1)for p in C):B.setdefault(c,[]).append((r0,c0,r1,c1))
 c=min(B,key=lambda k:(len(B[k]),k));r0,c0,r1,c1=B[c][0];h=r1-r0+1;w=c1-c0+1;iH=h-2;iW=w-2;R=[(x,y)for x in range(h)for y in range(w)if x in(0,h-1)or y in(0,w-1)]
 for i in range(n-iH+1):
  for j in range(n-iW+1):
   if all(g[i+x][j+y]==0 for x in range(iH)for y in range(iW)if x in(0,iH-1)or y in(0,iW-1)):
    for x,y in R:
     a=i-1+x;b=j-1+y
     if 0<=a<n and 0<=b<n:o[a][b]=c
 return o
