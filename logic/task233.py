def p(g):
 h=len(g);w=len(g[0]);G=[r[:]for r in g];c=[0]*10
 for v in sum(g,[]):c[v]+=v>0
 m=max(range(10),key=c.__getitem__)
 C=[]
 for i in range(h):
  for j in range(w):
   if g[i][j]:
    q=[(i,j)];g[i][j]=0;t=b=i;l=r=j;n=1
    while q:
     x,y=q.pop();t=min(t,x);b=max(b,x);l=min(l,y);r=max(r,y)
     for nx,ny in((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
      if 0<=nx<h and 0<=ny<w and g[nx][ny]:g[nx][ny]=0;q+=[(nx,ny)];n+=1
    C+=(n,t,b,l,r),
 C.sort();n,t,b,l,r=C.pop()
 W=r-l+1;H=b-t+1;o=[z[l:r+1]for z in G[t:b+1]];R=[[m]*W for _ in range(H)]
 for n,t,b,l,r in C:
  if (b-t+1)*(r-l+1)==n and (s:=sum(p:=[z[l:r+1]for z in G[t:b+1]],[])).count(m) and len({*s})>1:
   r=[p]
   for _ in'123':r+=[p:=[*zip(*p[::-1])]]
   for t in r+[[s[::-1]for s in q]for q in r]:
    h=len(t);w=len(t[0])
    S=[(i,j)for i in range(H-h+1)for j in range(W-w+1)if all((t[a][b]==m)==(o[i+a][j+b]==0)for a in range(h)for b in range(w))]
    if S:
     i,j=S[-1]
     if i*j*(i+h-H)*(j+w-W)==0:i,j=S[0]
     for a in range(h):R[i+a][j:j+w]=t[a];o[i+a][j:j+w]=[m]*w
     break
 return R
