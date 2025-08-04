def p(g):
 t=any(len({*r})>2 for r in g)
 if t:g=[list(r)for r in zip(*g)]
 h=len(g);w=len(g[0]);o=[r[:]for r in g];v=set()
 for i in range(h):
  for j in range(w):
   if g[i][j]and(i,j)not in v:
    c=g[i][j];q=[(i,j)];v.add((i,j));y0=y1=i;x0=x1=j
    while q:
     y,x=q.pop()
     for a,b in((1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)):
      r=y+a;s=x+b
      if 0<=r<h and 0<=s<w and g[r][s]==c and(r,s)not in v:v.add((r,s));q.append((r,s));y0=min(y0,r);y1=max(y1,r);x0=min(x0,s);x1=max(x1,s)
    for x in range(x0,x1+1):
     if any(g[y][x]==0 for y in range(y0,y1+1)):
      for y in range(y0,y1+1):o[y][x]=0
 if t:o=[list(r)for r in zip(*o)]
 return o
