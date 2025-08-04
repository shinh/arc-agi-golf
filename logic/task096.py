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
 mets=[]
 for c,s in patches.items():
  sy,sx,ey,ex=bbox(s)
  shape=max(ey-sy+1,ex-sx+1)
  mx=max(max(x for _,x in cc)-min(x for _,x in cc)+1 for cc in comps[c])
  mets.append((-(shape+mx),-c,c))
 cols=[c for _,__,c in sorted(mets)]
 def norm(s):
  sy=min(y for y,x in s);sx=min(x for y,x in s)
  return {(y-sy,x-sx) for y,x in s}
 def vm(s):
  sy,sx,ey,ex=bbox(s)
  return {(y,sx+ex-x) for y,x in s}
 def hm(s):
  sy,sx,ey,ex=bbox(s)
  return {(sy+ey-y,x) for y,x in s}
 def cm(s):
  sy,sx,ey,ex=bbox(s)
  return {(sy+ey-y,sx+ex-x) for y,x in s}
 orient=[]
 for c in cols:
  S=patches[c]
  best=None;sc=-1
  for s in(S,vm(S),cm(S),hm(S)):
   n=norm(s);score=((1,0) in n)+((0,1) in n)
   if score>sc:sc=score;best=n
  orient.append((c,best))
 counts=[len(patches[c]) for c in cols]
 n=len(cols)+(0 if any(k==1 for k in counts) else 1)
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
