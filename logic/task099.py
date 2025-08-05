def p(g):
 h=w=10;v=[[0]*w for _ in g];B=[]
 for y in range(h):
  for x in range(w):
   if g[y][x]==1 and not v[y][x]:
    q=[(y,x)];v[y][x]=1;R=[];C=[]
    while q:
     i,j=q.pop();R+=[i];C+=[j]
     for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
      ni=i+dy;nj=j+dx
      if 0<=ni<h and 0<=nj<w and g[ni][nj]==1 and not v[ni][nj]:v[ni][nj]=1;q+=[(ni,nj)]
    B+=[(min(R),max(R),min(C),max(C))]
 for y in range(h):
  for x in range(w):
   c=g[y][x]
   if c and c!=1:
    for a,b,l,r in B:
     if a<=y<=b and l<=x<=r:
      t=max(0,a-1);v=[[0]*w for _ in g];q=[(y,x)];v[y][x]=1
      while q:
       i,j=q.pop()
       for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
        ni=i+dy;nj=j+dx
        if t<=ni<=b and l<=nj<=r and g[ni][nj]==0 and not v[ni][nj]:v[ni][nj]=1;q+=[(ni,nj)]
      for i in range(h):
       for j in range(w):
        if v[i][j]:g[i][j]=c
      break
 return g
