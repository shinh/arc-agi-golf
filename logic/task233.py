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
 W=r-l+1;H=b-t+1;o=[z[l:r+1]for z in G[t:b+1]];R=[[m]*W for _ in range(H)];O=[]
 for n,t,b,l,r in C:
  if (b-t+1)*(r-l+1)==n and (S:=sum(p:=[z[l:r+1]for z in G[t:b+1]],[])).count(m) and len({*S})>1:O+=p,
 for P in O:
  r=[P]
  for _ in'123':r+=[P:=[*zip(*P[::-1])]]
  for t in r+[[s[::-1]for s in q]for q in r]:
   ph,pw=len(t),len(t[0])
   S=[(i,j)for i in range(H-ph+1)for j in range(W-pw+1)if all((t[a][b]==m)==(o[i+a][j+b]==0)for a in range(ph)for b in range(pw))]
   if S:
    i,j=S[-1]
    if i*j*(i+ph-H)*(j+pw-W)==0:i,j=S[0]
    for a in range(ph):R[i+a][j:j+pw]=t[a];o[i+a][j:j+pw]=[m]*pw
    break
 return R

