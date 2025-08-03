def p(g):
 h=len(g);w=len(g[0]);v=set()
 for y in range(h):
  for x in range(w):
   if g[y][x]-1 or (y,x)in v:continue
   q=[(y,x)];v.add((y,x));c=[]
   while q:
    y0,x0=q.pop();c.append((y0,x0))
    for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
     ny, nx=y0+dy,x0+dx
     if 0<=ny<h and 0<=nx<w and g[ny][nx]==1 and (ny,nx)not in v:v.add((ny,nx));q.append((ny,nx))
   ys=[i for i,_ in c];xs=[j for _,j in c]
   a,b,c1,d=min(ys),min(xs),max(ys),max(xs)
   sub=[r[b:d+1] for r in g[a:c1+1]]
   if len(sub)*len(sub[0])>len(c) and all(x==1 for x in sub[0]+sub[-1]+[r[0]for r in sub]+[r[-1]for r in sub]):
    for y0,x0 in c:g[y0][x0]=3
 return g
