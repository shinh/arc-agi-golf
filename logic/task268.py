def p(g):# fill bbox & rays
 Y,X=zip(*[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v]);t,b=min(Y),max(Y);l,R=min(X),max(X);s=[]
 for i in range(t,b+1):
  r=g[i]
  for j in range(l,R+1):
   if r[j]<1:r[j]=4;s+=((i,j),)*(i in(t,b)or j in(l,R))
 if s:
  Y,X=zip(*s);u,v=min(Y),max(Y);x,y=min(X),max(X);k=[u-t,x-l,v-b,0].index(0)
  P=[(u,y),(u,x),(v,x),(v,y)];D=[(-1,1),(-1,-1),(1,-1),(1,1)];d3=[(-1,0),(0,-1),(1,0),(0,1)][k]
  for p,d in((P[k],D[k]),(P[k-3],D[k-3]),*[(p,d3)for p in s]):
   i,j=p;di,dj=d
   while len(g)>i>=0<=j<len(g[0]):g[i][j]=4;i+=di;j+=dj
 return g
