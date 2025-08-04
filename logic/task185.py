def p(g):
 h=len(g);w=len(g[0]);v=[[0]*w for _ in g];C=[0]*10;A=M=0
 for y in range(h):
  for x in range(w):
   k=g[y][x];C[k]+=1
   if v[y][x]:continue
   v[y][x]=1;q=[y,x];n=0;a=b=y;c=d=x
   while q:
    j=q.pop();i=q.pop();n+=1
    a=min(a,i);b=max(b,i);c=min(c,j);d=max(d,j)
    for Y,X in((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
     if 0<=Y<h and 0<=X<w and not v[Y][X] and g[Y][X]==k:v[Y][X]=1;q+=Y,X
   if n==(e:=(b-a+1)*(d-c+1))>M:A=k;M=e
 C[A]=0;B=C.index(max(C))
 a=h;b=0;c=w;d=0
 for i,r in enumerate(g):
  for j,k in enumerate(r):
   if k not in(A,B):a=min(a,i);b=max(b,i);c=min(c,j);d=max(d,j)
 s=[r[c:d+1]for r in g[a:b+1]]
 h,w=len(s),len(s[0]);v=[[0]*w for _ in s];P=[]
 for y in range(h):
  for x in range(w):
   if v[y][x] or s[y][x]!=A:continue
   v[y][x]=1;q=[y,x];a=b=y;c=d=x
   while q:
    j=q.pop();i=q.pop()
    for Y,X in((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
     if 0<=Y<h and 0<=X<w and not v[Y][X] and s[Y][X]==A:
      v[Y][X]=1;q+=Y,X
      a=min(a,Y);b=max(b,Y);c=min(c,X);d=max(d,X)
   P+=[[a,c,b,d]]
 P.sort();R=[];i=0
 while i<len(P):
  t=P[i][0];row=[]
  while i<len(P) and P[i][0]==t:
   a,c,b,d=P[i];i+=1
   f={s[u][v]for u,v in((a-1,c-1),(a-1,d+1),(b+1,c-1),(b+1,d+1))if 0<=u<h and 0<=v<w}
   row+=[(len(f)==1 and not f&{A,B} and f.pop()) or A]
  R+=row,
 return R
