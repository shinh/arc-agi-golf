def p(g):
 h=len(g);w=len(g[0])
 for y in range(h):
  for x in range(w):
   if g[y][x]==2:
    q=[(y,x)];g[y][x]=0;r0=r1=y;c0=c1=x
    while q:
     y1,x1=q.pop()
     if y1<r0:r0=y1
     if y1>r1:r1=y1
     if x1<c0:c0=x1
     if x1>c1:c1=x1
     for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
      ny=y1+dy;nx=x1+dx
      if 0<=ny<h and 0<=nx<w and g[ny][nx]==2:
       g[ny][nx]=0;q.append((ny,nx))
    if r1>r0+1 and c1>c0+1:
     for yy in range(r0+1,r1):
      for xx in range(c0+1,c1):g[yy][xx]=3
 return g
