def p(g):
 h=len(g);w=len(g[0])
 sr=next(i for i in range(1,h)if len(set(g[i]))==1)+1
 sc=next(j for j in range(1,w)if len({g[k][j]for k in range(h)})==1)+1
 B=[r[::sc]for r in g[::sr]];H=len(B);W=len(B[0])
 f=sum(B,[]);bg=max(f,key=f.count)
 D=(1,0,-1,0,1);S=set();objs=[]
 for i in range(H):
  for j in range(W):
   if(i,j)in S or B[i][j]==bg:continue
   q=[(i,j)];S.add((i,j));o=[]
   while q:
    y,x=q.pop();o.append((y,x))
    for k in range(4):
     ny=y+D[k];nx=x+D[k+1]
     if 0<=ny<H and 0<=nx<W and(ny,nx)not in S and B[ny][nx]!=bg:S.add((ny,nx));q.append((ny,nx))
   objs.append(o)
 if not objs:return g
 obj=max(objs,key=lambda o:len({B[y][x]for y,x in o}))
 oth=[o for o in objs if o is not obj]
 cols=[B[y][x]for y,x in obj]
 t=oth and B[oth[0][0][0]][oth[0][0][1]]
 c=t if t in cols else min(set(cols),key=cols.count)
 mn=min(y for y,_ in obj);ml=min(x for _,x in obj)
 pat=[(B[y][x],y-mn,x-ml)for y,x in obj]
 ay,ax=min((y,x)for col,y,x in pat if col==c)
 pat=[(col,y-ay,x-ax)for col,y,x in pat]
 S=set();tgt=[]
 for i in range(H):
  for j in range(W):
   if(i,j)in S or B[i][j]!=c:continue
   q=[(i,j)];S.add((i,j));my=i;mx=j
   while q:
    y,x=q.pop()
    for k in range(4):
     ny=y+D[k];nx=x+D[k+1]
     if 0<=ny<H and 0<=nx<W and(ny,nx)not in S and B[ny][nx]==c:
      S.add((ny,nx));q.append((ny,nx))
      if ny<my:my=ny
      if nx<mx:mx=nx
   tgt.append((my,mx))
 for ty,tx in tgt:
  for col,dy,dx in pat:
   y,x=ty+dy,tx+dx
   if 0<=y<H and 0<=x<W:B[y][x]=col
 out=[r[:]for r in g]
 for bi in range(H):
  for bj in range(W):
   v=B[bi][bj];r0=bi*sr;c0=bj*sc
   for i in range(sr-1):
    for j in range(sc-1):out[r0+i][c0+j]=v
 return out

