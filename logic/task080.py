def p(g):
 m=len(g);n=len(g[0])
 a=next(i for i in range(1,m)if len(set(g[i]))==1)+1
 b=next(j for j in range(1,n)if len({r[j]for r in g})==1)+1
 B=[r[::b]for r in g[::a]];h=len(B);w=len(B[0])
 d=(1,0,-1,0,1);s=set();f=0
 for i in range(h):
  for j in range(w):
   if B[i][j]and(i,j)not in s:
    q=[(i,j)];s.add((i,j));o=[];col=[]
    while q:
     y,x=q.pop();o.append((y,x));col.append(B[y][x])
     for k in range(4):
      ny=y+d[k];nx=x+d[k+1]
      if 0<=ny<h and 0<=nx<w and B[ny][nx]and(ny,nx)not in s:s.add((ny,nx));q.append((ny,nx))
    if len(set(col))>1:obj=o;f=1;break
  if f:break
 t=0;f=0
 for i in range(h):
  for j in range(w):
   if B[i][j]and(i,j)not in s:t=B[i][j];f=1;break
  if f:break
 c=t if t in col else min(col,key=col.count)
 mn=min(y for y,_ in obj);mx=min(x for _,x in obj)
 pat=[(B[y][x],y-mn,x-mx)for y,x in obj]
 ay,ax=min((y,x)for k,y,x in pat if k==c)
 pat=[(k,y-ay,x-ax)for k,y,x in pat]
 for y in range(h):
  for x in range(w):
   if B[y][x]==c and(y==0 or B[y-1][x]!=c)and(x==0 or B[y][x-1]!=c):
    for k,dy,dx in pat:
     Y=y+dy;X=x+dx
     if 0<=Y<h and 0<=X<w:B[Y][X]=k
 for i in range(m):
  for j in range(n):
   if i%a<a-1 and j%b<b-1:g[i][j]=B[i//a][j//b]
 return g

