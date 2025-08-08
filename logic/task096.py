def p(g):
 H=len(g);W=len(g[0]);R=lambda g:[list(r)for r in zip(*g[::-1])]
 p=[set()for _ in[0]*10]
 for y,r in enumerate(g):
  for x,v in enumerate(r):p[v].add((y,x))
 B=max(range(10),key=lambda c:len(p[c]))
 V=[[0]*W for _ in g];m=[0]*10
 for y in range(H):
  for x in range(W):
   if V[y][x] or g[y][x]==B:continue
   c=g[y][x];V[y][x]=1;st=[(y,x)];mn=mx=x
   while st:
    cy,cx=st.pop();mn=min(mn,cx);mx=max(mx,cx)
    for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
     ny,nx=cy+dy,cx+dx
     if 0<=ny<H and 0<=nx<W and not V[ny][nx] and g[ny][nx]==c:
      V[ny][nx]=1;st.append((ny,nx))
   m[c]=max(m[c],mx-mn+1)
 parts={frozenset((c,(y,x))for y,x in s)for c,s in enumerate(p) if s and c!=B}
 def bb(s):
  ys,xs=zip(*((y,x)for _,(y,x) in s));return min(ys),min(xs),max(ys),max(xs)
 def norm(s):
  sy,sx=bb(s)[:2];return {(i-sy,j-sx)for _,(i,j) in s}
 def vm(s):
  sy,sx,ey,ex=bb(s);return frozenset((v,(i,sx+ex-j))for v,(i,j) in s)
 def hm(s):
  sy,sx,ey,ex=bb(s);return frozenset((v,(sy+ey-i,j))for v,(i,j) in s)
 def cm(s):
  sy,sx,ey,ex=bb(s);return frozenset((v,(sy+ey-i,sx+ex-j))for v,(i,j) in s)
 sc={};tmp=[]
 for P in parts:
  c=next(iter(P))[0];sy,sx,ey,ex=bb(P)
  sc[c]=max(ey-sy+1,ex-sx+1)+m[c]
  tmp.append((-sc[c],P))
 x9=[p for _,p in sorted(tmp)]
 if sc.get(2)==sc.get(4)==max(sc.values()):
  pos={next(iter(p))[0]:i for i,p in enumerate(x9)}
  if pos[2]<pos[4]:x9[pos[2]],x9[pos[4]]=x9[pos[4]],x9[pos[2]]
 shp=[]
 for P in x9:
  b=max({P,vm(P),cm(P),hm(P)},key=lambda t:((1,0)in norm(t))+((0,1)in norm(t)))
  shp.append((next(iter(b))[0],norm(b)))
 L=2*(len(x9)+all(len(p)-1 for p in x9))-1
 sft=[(c,{(y+i,x+i)for y,x in s})for i,(c,s) in enumerate(shp)]
 o=[[B]*L for _ in range(L)]
 for _ in range(4):
  for c,s in sft:
   for y,x in s:o[y][x]=c
  if _<3:o=R(o)
 return o
