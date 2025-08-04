def p(g):
 h=len(g);w=len(g[0])
 f=[c for r in g for c in r];bg=max(set(f),key=f.count)
 v=[[0]*w for _ in g];o=[]
 for i in range(h):
  for j in range(w):
   if g[i][j]==bg or v[i][j]:continue
   q=[(i,j)];v[i][j]=1;u=[]
   while q:
    x,y=q.pop();u+=[(g[x][y],x,y)]
    for dx,dy in((1,0),(-1,0),(0,1),(0,-1)):
     nx,ny=x+dx,y+dy
     if 0<=nx<h and 0<=ny<w and g[nx][ny]!=bg and not v[nx][ny]:
      v[nx][ny]=1;q+=[(nx,ny)]
   o+=[u]
 pal=set(f);cand=[]
 for c in pal:
  if all(1<=sum(v==c for v,_,_ in u)<=2 for u in o):cand+=[c]
 sp=min(cand,key=f.count)
 o.sort(key=lambda u:min(y for _,_,y in u))
 r=[];a=None
 for u in o:
  spc=[(i,j)for v,i,j in u if v==sp]
  oth=[(v,i,j)for v,i,j in u if v!=sp]
  if oth:
   col=[v for v,_,_ in oth];m=max(set(col),key=col.count)
  else:m=bg
  if a==None:
   r+=oth+[(m,i,j)for i,j in spc]
   a=max(spc)
  else:
   ac=min(spc,key=lambda p:(abs(p[0]-a[0])+abs(p[1]-a[1]),p[1],p[0]))
   di=a[0]-ac[0];dj=a[1]-ac[1]+1
   oth=[(v,i+di,j+dj)for v,i,j in oth]
   spc=[(i+di,j+dj)for i,j in spc]
   r+=oth+[(m,i,j)for i,j in spc]
   ac=(ac[0]+di,ac[1]+dj)
   rem=[p for p in spc if p!=ac]
   a=max(rem) if rem else ac
 if not r:return g
 mi=min(j for _,_,j in r);ma=max(j for _,_,j in r);w2=ma-mi+1
 out=[[bg]*w2 for _ in range(h)]
 for v,i,j in r:
  j-=mi
  if 0<=i<h and 0<=j<w2:out[i][j]=v
 return out
