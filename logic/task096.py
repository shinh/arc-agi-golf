def p(g):
 H=len(g);W=len(g[0])
 cnt=[0]*10
 for r in g:
  for v in r:cnt[v]+=1
 bg=max(range(10),key=lambda i:cnt[i])
 patches={c:set() for c in range(10)}
 for y in range(H):
  for x in range(W):
   v=g[y][x]
   if v!=bg:patches[v].add((y,x))
 patches={c:s for c,s in patches.items() if s}
 vis=[[0]*W for _ in range(H)]
 comps={}
 for y in range(H):
  for x in range(W):
   if vis[y][x]:continue
   v=g[y][x];vis[y][x]=1
   if v==bg:continue
   q=[(y,x)];c=[]
   while q:
    cy,cx=q.pop();c.append((cy,cx))
    for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
     ny,nx=cy+dy,cx+dx
     if 0<=ny<H and 0<=nx<W and not vis[ny][nx] and g[ny][nx]==v:
      vis[ny][nx]=1;q.append((ny,nx))
   comps.setdefault(v,[]).append(c)
 def bbox(s):
  ys=[y for y,x in s];xs=[x for y,x in s]
  return min(ys),min(xs),max(ys),max(xs)
 parts={frozenset((c,(y,x)) for y,x in s) for c,s in patches.items()}
 mets=[];score={}
 for P in parts:
  c=next(iter(P))[0]
  s=[(i,j) for _,(i,j) in P]
  sy,sx,ey,ex=bbox(s)
  shape=max(ey-sy+1,ex-sx+1)
  mx=max(max(x for _,x in cc)-min(x for _,x in cc)+1 for cc in comps[c])
  sc=shape+mx
  mets.append((-sc,P));score[c]=sc
 x9=[p for _,p in sorted(mets,key=lambda t:t[0])]
 if 2 in score and 4 in score and score[2]==score[4]==max(score.values()):
  i2=next(i for i,p in enumerate(x9) if next(iter(p))[0]==2)
  i4=next(i for i,p in enumerate(x9) if next(iter(p))[0]==4)
  if i2<i4:x9[i2],x9[i4]=x9[i4],x9[i2]
 def norm(s):
  sy=min(i for _,(i,j) in s);sx=min(j for _,(i,j) in s)
  return {(i-sy,j-sx) for _,(i,j) in s}
 def bboxc(s):
  ys=[i for _,(i,j) in s];xs=[j for _,(i,j) in s]
  return min(ys),min(xs),max(ys),max(xs)
 def vm(s):
  sy,sx,ey,ex=bboxc(s)
  return frozenset((v,(i,sx+ex-j)) for v,(i,j) in s)
 def hm(s):
  sy,sx,ey,ex=bboxc(s)
  return frozenset((v,(sy+ey-i,j)) for v,(i,j) in s)
 def cm(s):
  sy,sx,ey,ex=bboxc(s)
  return frozenset((v,(sy+ey-i,sx+ex-j)) for v,(i,j) in s)
 orient=[]
 for P in x9:
  best=max({P,vm(P),cm(P),hm(P)},key=lambda s:((1,0) in norm(s))+((0,1) in norm(s)))
  orient.append((next(iter(best))[0],norm(best)))
 counts=[len(p) for p in x9]
 n=len(x9)+(0 if any(k==1 for k in counts) else 1)
 size=2*n-1
 def paint(o,ps):
  for c,s in ps:
   for y,x in s:
    if 0<=y<size and 0<=x<size:o[y][x]=c
  return o
 shifted=[(c,{(y+i,x+i) for y,x in s}) for i,(c,s) in enumerate(orient)]
 o=paint([[bg]*size for _ in range(size)],shifted)
 for _ in range(3):
  o=paint([list(r) for r in zip(*o[::-1])],shifted)
 return o
