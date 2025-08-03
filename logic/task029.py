def p(g):
 h=len(g);w=len(g[0]);V=set()
 for y in range(h):
  for x in range(w):
   if(y,x)in V:continue
   c=g[y][x];S=[(y,x)];V.add((y,x));a=b=y;d=e=x;n=0
   while S:
    y1,x1=S.pop();n+=1;a=min(a,y1);b=max(b,y1);d=min(d,x1);e=max(e,x1)
    for u,v in((1,0),(-1,0),(0,1),(0,-1)):
     ny,nx=y1+u,x1+v
     if 0<=ny<h and 0<=nx<w and (ny,nx)not in V and g[ny][nx]==c:V.add((ny,nx));S.append((ny,nx))
   if e-d>1 and b-a>1 and n==2*(e-d+b-a):return[r[d+1:e]for r in g[a+1:b]]
