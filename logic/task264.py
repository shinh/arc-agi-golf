def p(g):
 a=sum(g,[]);b=max(a,key=a.count);l=max({v for v in a if v!=b},key=a.count);h=len(g);w=len(g[0]);o=[[l]*9 for _ in range(9)]
 for i in range(h):
  for j in range(w):
   c=g[i][j]
   if c in(b,l):continue
   q=[(i,j)];g[i][j]=b;s=[]
   while q:
    x,y=q.pop();s+=[(x,y)]
    for X,Y in((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
     if 0<=X<h and 0<=Y<w and g[X][Y]==c:g[X][Y]=b;q+=[(X,Y)]
   u,v=zip(*s);mi=min(u);mj=min(v);s=[(x-mi,y-mj)for x,y in s];u,v=zip(*s);n=len(s)
   if n==3:a=8-6*(2-sum(u))-2*(2-sum(v));P=[a,a+1-2*(a%3>0),a+3-6*(a>2)]
   else:
    if max(u)<max(v):a=1 if sum(u)<3 else 7;P=[a-1,a,a+1,4]
    else:a=3 if sum(v)<3 else 5;P=[a-3,a,a+3,4]
   r,k=divmod(a,3);R=r*3;C=k*3
   for t in P:d,e=divmod(t,3);o[R+d][C+e]=c
 return o

