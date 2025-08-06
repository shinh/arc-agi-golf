def p(g):
 H=len(g);W=len(g[0])
 pts=[[]for _ in range(10)]
 for y,r in enumerate(g):
  for x,v in enumerate(r):pts[v].append((y,x))
 bg=max(range(10),key=lambda c:len(pts[c]))
 pts={c:s for c,s in enumerate(pts) if s and c!=bg}
 vis=[[0]*W for _ in g];wid={c:0 for c in pts}
 for y in range(H):
  for x in range(W):
   if vis[y][x] or g[y][x]==bg:continue
   v=g[y][x];vis[y][x]=1;st=[(y,x)];mn=mx=x
   while st:
    cy,cx=st.pop();mn=min(mn,cx);mx=max(mx,cx)
    for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
     ny,nx=cy+dy,cx+dx
     if 0<=ny<H and 0<=nx<W and not vis[ny][nx] and g[ny][nx]==v:
      vis[ny][nx]=1;st.append((ny,nx))
   wid[v]=max(wid[v],mx-mn+1)
 def bb(s):
  ys=[y for _,(y,_) in s];xs=[x for _,(_,x) in s];return min(ys),min(xs),max(ys),max(xs)
 def norm(s):
  sy,sx=bb(s)[:2];return {(i-sy,j-sx)for _,(i,j) in s}

 def vm(s):
  sy,sx,ey,ex=bb(s);return frozenset((v,(i,sx+ex-j))for v,(i,j) in s)
 def hm(s):
  sy,sx,ey,ex=bb(s);return frozenset((v,(sy+ey-i,j))for v,(i,j) in s)
 def cm(s):
  sy,sx,ey,ex=bb(s);return frozenset((v,(sy+ey-i,sx+ex-j))for v,(i,j) in s)
 parts={frozenset((c,(y,x))for y,x in set(s))for c,s in pts.items()}
 mets=[];sc={}
 for P in parts:
  c=next(iter(P))[0]
  sy,sx,ey,ex=bb(P)

  sc[c]=max(ey-sy+1,ex-sx+1)+wid[c]
  mets.append((-sc[c],P))
 x9=[p for _,p in sorted(mets)]
 if 2 in sc and 4 in sc and sc[2]==sc[4]==max(sc.values()):
  i2=next(i for i,p in enumerate(x9) if next(iter(p))[0]==2)
  i4=next(i for i,p in enumerate(x9) if next(iter(p))[0]==4)
  if i2<i4:x9[i2],x9[i4]=x9[i4],x9[i2]
 shp=[]
 for P in x9:
  b=max({P,vm(P),cm(P),hm(P)},key=lambda t:((1,0)in norm(t))+((0,1)in norm(t)))
  shp.append((next(iter(b))[0],norm(b)))
 L=2*(len(x9)+(1 not in [len(p)for p in x9]))-1
 def paint(o,ps):
  for c,s in ps:
   for y,x in s:o[y][x]=c
  return o
 sft=[(c,{(y+i,x+i)for y,x in s})for i,(c,s) in enumerate(shp)]
 o=paint([[bg]*L for _ in range(L)],sft)
 for _ in range(3):o=paint([list(r)for r in zip(*o[::-1])],sft)
 return o
