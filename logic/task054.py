def p(g):
 h=[r[:]for r in g];b=g[0][0];R=[];V=set()
 for y in range(30):
  for x in range(30):
   if g[y][x]!=b and(y,x)not in V:
    c=g[y][x];S={(y,x)};V.add((y,x));q=[(y,x)]
    while q:
     y0,x0=q.pop()
     for Y,X in((y0+1,x0),(y0-1,x0),(y0,x0+1),(y0,x0-1)):
      if 0<=Y<30 and 0<=X<30 and g[Y][X]==c and(Y,X)not in S:
       S.add((Y,X));q.append((Y,X));V.add((Y,X))
    ys,xs=zip(*S);y0=min(ys);y1=max(ys);x0=min(xs);x1=max(xs);n=len(S)
    if n>20 and(y1-y0+1)*(x1-x0+1)-n<5:R+=[(y0,y1,x0,x1,c)]
 P=[(y,x)for y in range(30)for x in range(30)if g[y][x]!=b and not any(y0<=y<=y1 and x0<=x<=x1 for y0,y1,x0,x1,_ in R)]
 for y,x in P:h[y][x]=b
 ys,xs=zip(*P);my,My=min(ys),max(ys);mx,Mx=min(xs),max(xs)
 A=[[b]*(Mx-mx+1)for _ in range(My-my+1)]
 for y,x in P:A[y-my][x-mx]=g[y][x]
 H=len(A);W=len(A[0]);cy=H//2;cx=W//2;cen=A[cy][cx];C=[]
 for dy,dx in((-1,0),(0,1),(1,0),(0,-1)):
  y,x=cy+dy,cx+dx
  if 0<=y<H and 0<=x<W and A[y][x]!=b:
   c=A[y][x];y+=dy;x+=dx;C+=[c,0<=y<H and 0<=x<W and A[y][x]==c]
  else:C+=[b,0]
 for y0,y1,x0,x1,c in R:
  for y in range(y0,y1+1):
   for x in range(x0,x1+1):
    if g[y][x]!=c:
     for dy,r in enumerate(A):
      ty=y-cy+dy
      if y0<=ty<=y1:
       u=h[ty]
       for dx,val in enumerate(r):
        tx=x-cx+dx
        if x0<=tx<=x1:u[tx]=c if val==b else val
     if C[1]:
      for Y in range(y0,y):h[Y][x]=C[0]
     if C[3]:
      for X in range(x+1,x1+1):h[y][X]=C[2]
     if C[5]:
      for Y in range(y+1,y1+1):h[Y][x]=C[4]
     if C[7]:
      for X in range(x0,x):h[y][X]=C[6]
     h[y][x]=cen
 return h
