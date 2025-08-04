def p(g):
 h=len(g);w=len(g[0]);v=[[0]*w for _ in g];cnt={};c0=M=0
 for y in range(h):
  for x in range(w):
   if v[y][x]:continue
   c=g[y][x];q=[(y,x)];v[y][x]=1;n=0;y0=y1=y;x0=x1=x
   while q:
    i,j=q.pop();n+=1
    if i<y0:y0=i
    if i>y1:y1=i
    if j<x0:x0=j
    if j>x1:x1=j
    for a,b in((1,0),(-1,0),(0,1),(0,-1)):
     ni=i+a;nj=j+b
     if 0<=ni<h and 0<=nj<w and not v[ni][nj] and g[ni][nj]==c:v[ni][nj]=1;q+=[(ni,nj)]
   cnt[c]=cnt.get(c,0)+n;A=(y1-y0+1)*(x1-x0+1)
   if n==A and A>M:M=A;c0=c
 c1=max((k for k in cnt if k!=c0),key=cnt.get)
 a=h;b=0;c=w;d=0
 for i,r in enumerate(g):
  for j,u in enumerate(r):
   if u not in(c0,c1):
    if i<a:a=i
    if i>b:b=i
    if j<c:c=j
    if j>d:d=j
 s=[r[c:d+1]for r in g[a:b+1]];h=len(s);w=len(s[0]);v=[[0]*w for _ in s];P=[]
 for y in range(h):
  for x in range(w):
   if v[y][x]or s[y][x]!=c0:continue
   q=[(y,x)];v[y][x]=1;t=b=y;l=r=x
   while q:
    i,j=q.pop()
    if i<t:t=i
    if i>b:b=i
    if j<l:l=j
    if j>r:r=j
    for a,b1 in((1,0),(-1,0),(0,1),(0,-1)):
     ni=i+a;nj=j+b1
     if 0<=ni<h and 0<=nj<w and not v[ni][nj]and s[ni][nj]==c0:v[ni][nj]=1;q+=[(ni,nj)]
   P+=[(t,b,l,r)]
 P.sort();R=[];m=-1
 for t,b,l,r in P:
  if t!=m:R+=[[]];m=t
  k=[s[i][j]for i,j in((t-1,l-1),(t-1,r+1),(b+1,l-1),(b+1,r+1))if 0<=i<h and 0<=j<w]
  R[-1]+=[k[0]if k and len(set(k))==1 and k[0]not in(c0,c1)else c0]
 return R

