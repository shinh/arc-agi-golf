def p(g):# fill bbox & rays
 h=len(g);w=len(g[0])
 f=[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v]
 si,sj=zip(*f);t,b=min(si),max(si);l,R=min(sj),max(sj)
 s=[]
 for i in range(t,b+1):
  for j in range(l,R+1):
   if g[i][j]<1:
    g[i][j]=4
    if i in(t,b)or j in(l,R):s+=(i,j),
 if s:
  si,sj=zip(*s);u,v=min(si),max(si);x,y=min(sj),max(sj);k=[u==t,x==l,v==b,1].index(1)
  S=u,y,u,x,v,x,v,y,u,y;a=S[k*2:k*2+2];b=S[k*2+2:k*2+4]
  A=[(-1,1,-1,-1,-1,0),(-1,-1,1,-1,0,-1),(1,-1,1,1,1,0),(1,1,-1,1,0,1)][k];d1=A[:2];d2=A[2:4];d3=A[4:]
  for p,d in((a,d1),(b,d2),*[(p,d3)for p in s]):
   i,j=p;di,dj=d
   while h>i>=0<=j<w:g[i][j]=4;i+=di;j+=dj
 return g
