def p(g):
 h=w=10
 v=[[0]*w for _ in g];objs=[]
 for y in range(h):
  for x in range(w):
   if not v[y][x]:
    c=g[y][x];s=[(y,x)];v[y][x]=1;r=[]
    while s:
     i,j=s.pop();r.append((i,j))
     for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
      ny,nx=i+dy,j+dx
      if 0<=ny<h and 0<=nx<w and not v[ny][nx] and g[ny][nx]==c:
       v[ny][nx]=1;s.append((ny,nx))
    objs.append((c,r))
 def size(r):
  ys=[i for i,_ in r];xs=[j for _,j in r]
  return max(max(ys)-min(ys)+1,max(xs)-min(xs)+1)
 s=min(objs,key=lambda t:size(t[1]))
 sc=s[0]
 oc=({c for c,_ in objs}-{sc}).pop()
 O=[r for c,r in objs if c==oc]
 a=min(O,key=size);O.remove(a)
 def dist(r):
  return min(abs(i-x)+abs(j-y) for i,j in r for x,y in a)
 b=min(O,key=dist)
 r=lambda R:max(x for _,x in R)
 l=lambda R:min(x for _,x in R)
 u=lambda R:min(y for y,_ in R)
 d=lambda R:max(y for y,_ in R)
 hd=max(r(b)-r(a),l(a)-l(b))
 vd=max(d(b)-d(a),u(a)-u(b))
 ul=(u(a),l(a));lr=(d(a),r(a))
 o=[row[:] for row in g]
 for n in range(1,16):
  top=ul[0]-vd*n;left=ul[1]-hd*n;bot=lr[0]+vd*n;right=lr[1]+hd*n
  for j in range(left,right+1):
   if 0<=top<h and 0<=j<w:o[top][j]=oc
   if 0<=bot<h and 0<=j<w:o[bot][j]=oc
  for i in range(top,bot+1):
   if 0<=i<h and 0<=left<w:o[i][left]=oc
   if 0<=i<h and 0<=right<w:o[i][right]=oc
 for y in range(h):
  for x in range(w):
   if o[y][x]==sc:o[y][x]=5
 return o
