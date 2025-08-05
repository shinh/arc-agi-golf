def p(g):
 C=[0]*10
 for r in g:
  for k in r:C[k]+=1
 C[0]=0;B=C.index(max(C))
 a=len(g);b=0;c=len(g[0]);d=0
 for i,r in enumerate(g):
  for j,k in enumerate(r):
   if k and k-B:a=min(a,i);b=max(b,i);c=min(c,j);d=max(d,j)
 s=[r[c:d+1]for r in g[a:b+1]]
 h,w=len(s),len(s[0]);v=[[0]*w for _ in s];P=[]
 for y in range(h):
  for x in range(w):
   if v[y][x] or s[y][x]:continue
   v[y][x]=1;q=[y,x];a=b=y;c=d=x
   while q:
    j=q.pop();i=q.pop()
    for Y,X in((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
     if 0<=Y<h and 0<=X<w and not v[Y][X] and s[Y][X]==0:
      v[Y][X]=1;q+=Y,X
      a=min(a,Y);b=max(b,Y);c=min(c,X);d=max(d,X)
   P+=[[a,c,b,d]]
 P.sort();R=[]
 for i in range(0,len(P),3):
  row=[]
  for a,c,b,d in P[i:i+3]:
   f={s[u][v]for u,v in((a-1,c-1),(a-1,d+1),(b+1,c-1),(b+1,d+1))if 0<=u<h and 0<=v<w}
   row+=len(f)==1 and B not in f and f.pop(),
  R+=row,
 return R
