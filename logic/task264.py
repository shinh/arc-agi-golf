def p(g):
 h,w,f=len(g),len(g[0]),{}
 for r in g:
  for v in r:f[v]=f.get(v,0)+1
 b,l=sorted(f,key=f.get)[-1:-3:-1]
 def cl(s):
  xs,ys=zip(*s);mi=min(xs);mj=min(ys)
  S={(x-mi,y-mj)for x,y in s};xs,ys=zip(*S)
  h=max(xs)+1;w=max(ys)+1
  if len(S)==3:
   (i,j),=({(0,0),(0,1),(1,0),(1,1)}-S)
   return[['LR','LL'],['UR','UL']][i][j]
  if all((0,j)in S for j in range(w)):return'T'
  if all((h-1,j)in S for j in range(w)):return'B'
  if all((i,0)in S for i in range(h)):return'L'
  return'R'
 M=dict(UL=(0,[0,1,3]),T=(1,[0,1,2,4]),UR=(2,[1,2,5]),
    L=(3,[0,3,6,4]),R=(5,[2,5,8,4]),
    LL=(6,[3,6,7]),B=(7,[6,7,8,4]),LR=(8,[5,7,8]))
 out=[[l]*9 for _ in range(9)]
 for i in range(h):
  for j in range(w):
   c=g[i][j]
   if c in(b,l):continue
   q=[(i,j)];g[i][j]=b;s=[]
   while q:
    x,y=q.pop();s+=[(x,y)]
    for nx,ny in((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
     if 0<=nx<h and 0<=ny<w and g[nx][ny]==c:
      g[nx][ny]=b;q.append((nx,ny))
   k=M[cl(s)];r,cx=divmod(k[0],3);rr=r*3;cc=cx*3
   for p in k[1]:dr,dc=divmod(p,3);out[rr+dr][cc+dc]=c
 return out

