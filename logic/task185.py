def p(g):
 h=len(g);w=len(g[0])
 v=[[0]*w for _ in g];O=[]
 for y in range(h):
  for x in range(w):
   if v[y][x]:continue
   c=g[y][x];v[y][x]=1;q=[(y,x)];o=[(c,y,x)]
   while q:
    i,j=q.pop()
    for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
     ny=i+dy;nx=j+dx
     if 0<=ny<h and 0<=nx<w and not v[ny][nx] and g[ny][nx]==c:v[ny][nx]=1;q+=[(ny,nx)];o+=[(c,ny,nx)]
   O+=[o]
 def bb(o):
  ys=[i for _,i,_ in o];xs=[j for _,_,j in o]
  a,b=min(ys),max(ys);c,d=min(xs),max(xs)
  return a,b,c,d,(b-a+1)*(d-c+1)
 R=[o for o in O if len(o)==bb(o)[4]]
 c0=max(R,key=lambda o:bb(o)[4])[0][0]
 d={}
 for r in g:
  for v in r:
   if v!=c0:d[v]=d.get(v,0)+1
 c1=max(d,key=d.get)
 pts=[(i,j)for i,r in enumerate(g) for j,v in enumerate(r) if v not in (c0,c1)]
 a=min(i for i,_ in pts);b=max(i for i,_ in pts);c=min(j for _,j in pts);d=max(j for _,j in pts)
 s=[r[c:d+1] for r in g[a:b+1]];h2=len(s);w2=len(s[0])
 v=[[0]*w2 for _ in s];P=[]
 for y in range(h2):
  for x in range(w2):
   if v[y][x] or s[y][x]!=c0:continue
   q=[(y,x)];v[y][x]=1;o=[]
   while q:
    i,j=q.pop();o+=[(i,j)]
    for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
     ny=i+dy;nx=j+dx
     if 0<=ny<h2 and 0<=nx<w2 and not v[ny][nx] and s[ny][nx]==c0:v[ny][nx]=1;q+=[(ny,nx)]
   P+=[o]
 def pal(o):
  ys=[i for i,_ in o];xs=[j for _,j in o]
  a,b=min(ys),max(ys);c,d=min(xs),max(xs)
  corners=[(a-1,c-1),(a-1,d+1),(b+1,c-1),(b+1,d+1)]
  return {s[i][j] for i,j in corners if 0<=i<h2 and 0<=j<w2}
 rows=sorted({min(i for i,_ in o) for o in P});res=[]
 for r in rows:
  row=[o for o in P if min(i for i,_ in o)==r]
  row.sort(key=lambda o:min(j for _,j in o))
  res.append([next(iter(p)) if (p:=pal(o)) and p.isdisjoint({c0,c1}) and len(p)==1 else c0 for o in row])
 return res
