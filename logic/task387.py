def p(g):
 h=len(g);w=len(g[0])
 v=[[0]*w for _ in g];objs=[];allc=[]
 for y in range(h):
  for x in range(w):
   if g[y][x] and not v[y][x]:
    c=g[y][x];s=[(y,x)];v[y][x]=1;r=[]
    while s:
     i,j=s.pop();r.append((i,j))
     for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
      ny,nx=i+dy,j+dx
      if 0<=ny<h and 0<=nx<w and not v[ny][nx] and g[ny][nx]==c:
       v[ny][nx]=1;s.append((ny,nx))
    objs.append((c,r));allc+=r
 o=[r[:] for r in g];pal=sorted({c for c,_ in objs})
 for c,r in objs:
  oc=min(x for x in pal if x!=c)
  ys=[i for i,_ in r];xs=[j for _,j in r]
  a,b,c1,d1=min(ys)-1,max(ys)+1,min(xs)-1,max(xs)+1
  for j in range(c1,d1+1):
   if 0<=a<h:o[a][j]=oc
   if 0<=b<h:o[b][j]=oc
  for i in range(a,b+1):
   if 0<=c1<w:o[i][c1]=oc
   if 0<=d1<w:o[i][d1]=oc
 if allc:
  ys=[i for i,_ in allc];xs=[j for _,j in allc]
  a,b,c1,d1=min(ys),max(ys),min(xs),max(xs)
  B={(a,j) for j in range(c1,d1+1)}|{(b,j) for j in range(c1,d1+1)}|{(i,c1) for i in range(a,b+1)}|{(i,d1) for i in range(a,b+1)}
  S=set(allc)
  for i,j in B-S:
   if min(abs(i-y)+abs(j-x) for y,x in S)%2<1:o[i][j]=5
 return o
