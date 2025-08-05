def p(g):
 h=w=10;bg=0;v=set();c=[]
 for i in range(h):
  for j in range(w):
   if g[i][j]!=bg and (i,j)not in v:
    q=[(i,j)];v.add((i,j));o=[]
    while q:
     x,y=q.pop();o.append((x,y))
     for dx in(-1,0,1):
      for dy in(-1,0,1):
       if dx or dy:
        nx,ny=x+dx,y+dy
        if 0<=nx<h and 0<=ny<w and g[nx][ny]!=bg and (nx,ny)not in v:
         v.add((nx,ny));q.append((nx,ny))
    c.append(o)
 sh=[];cnt={}
 for o in c:
  mi=min(i for i,_ in o);mj=min(j for _,j in o)
  s=frozenset((i-mi,j-mj)for i,j in o)
  sh.append(s);cnt[s]=cnt.get(s,0)+1
 t=min(range(len(c)),key=lambda i:cnt[sh[i]])
 r=[row[:] for row in g]
 for k,o in enumerate(c):
  col=2 if k==t else 1
  for i,j in o:r[i][j]=col
 return r
