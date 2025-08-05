def p(g):
 n=len(g);o=[r[:]for r in g];B=[0]*10;D=B[:]
 for i in range(n):
  for j in range(n):
   if (c:=g[i][j])<1:continue
   t=[(i,j)];C=[];g[i][j]=-1;r0=r1=i;c0=c1=j
   while t:
    x,y=t.pop();C+=x*n+y,;r0=min(r0,x);r1=max(r1,x);c0=min(c0,y);c1=max(c1,y)
    for u,v in((1,0),(0,1),(-1,0),(0,-1)):
     if n>(nx:=x+u)>=0<=(ny:=y+v)<n and g[nx][ny]==c:g[nx][ny]=-1;t+=(nx,ny),
   if r1-r0>1 and c1-c0>1 and len(C)==2*(r1-r0+c1-c0)and all(p//n in(r0,r1)or p%n in(c0,c1)for p in C):
    D[c]+=1;B[c]=B[c]or(r0,c0,r1,c1)
 c=min(range(10),key=lambda k:(D[k] or 99,k));r0,c0,r1,c1=B[c];h=r1-r0+1;w=c1-c0+1;iH=h-2;iW=w-2
 R=[(x,y)for x in range(h)for y in range(w) if x*y*(x-h+1)*(y-w+1)==0]
 for i in range(n-iH+1):
  for j in range(n-iW+1):
   if all(g[i+x][j+y]==0 for x in range(iH)for y in range(iW) if x*y*(x-iH+1)*(y-iW+1)==0):
    for x,y in R:
     if n>(a:=i+x-1)>=0<=(b:=j+y-1)<n:o[a][b]=c
 return o
