def p(g):# fill bbox & rays
 Y,X=zip(*[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v]);t,b=min(Y),max(Y);l,R=min(X),max(X)
 s=[]
 for i in range(t,b+1):
  for j in range(l,R+1):
   if g[i][j]<1:
    g[i][j]=4
    if i in(t,b)or j in(l,R):s+=(i,j),
 if s:
  Y,X=zip(*s);u,v=min(Y),max(Y);x,y=min(X),max(X);k=[u==t,x==l,v==b,1].index(1)
  P=[(u,y),(u,x),(v,x),(v,y)];a,b=P[k],P[k-3]
  D=[(-1,1),(-1,-1),(1,-1),(1,1)];d1,d2=D[k],D[k-3];d3=[(-1,0),(0,-1),(1,0),(0,1)][k]
  for p,d in((a,d1),(b,d2),*[(p,d3)for p in s]):
   i,j=p;di,dj=d
   while len(g)>i>=0<=j<len(g[0]):g[i][j]=4;i+=di;j+=dj
 return g
