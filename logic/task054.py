def p(g):
 h=[r[:]for r in g];Y=len(g);X=len(g[0]);B=g[0][0];v=[[0]*X for _ in g];R=[]
 for y in range(Y):
  for x in range(X):
   if g[y][x]!=B and not v[y][x]:
    c=g[y][x];q=[(y,x)];v[y][x]=1;n=0;y0=y1=y;x0=x1=x
    while q:
     Y0,X0=q.pop();n+=1
     if Y0<y0:y0=Y0
     if Y0>y1:y1=Y0
     if X0<x0:x0=X0
     if X0>x1:x1=X0
     for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
      ny,nx=Y0+dy,X0+dx
      if 0<=ny<Y and 0<=nx<X and g[ny][nx]==c and not v[ny][nx]:v[ny][nx]=1;q.append((ny,nx))
    if n>20 and (y1-y0+1)*(x1-x0+1)-n<5:R+=[(y0,y1,x0,x1,c)]
 P=[];my=Y;My=0;mx=X;Mx=0
 for y in range(Y):
  for x in range(X):
   if g[y][x]!=B and not any(y0<=y<=y1 and x0<=x<=x1 for y0,y1,x0,x1,_ in R):
    P+=[(y,x)];h[y][x]=B
    if y<my:my=y
    if y>My:My=y
    if x<mx:mx=x
    if x>Mx:Mx=x
 pat=[[B]*(Mx-mx+1)for _ in range(My-my+1)]
 for y,x in P:pat[y-my][x-mx]=g[y][x]
 cy,cx=(len(pat)-1)//2,(len(pat[0])-1)//2;cen=pat[cy][cx];ph,pw=len(pat),len(pat[0])
 def a(dy,dx):
  y,x=cy+dy,cx+dx
  if 0<=y<ph and 0<=x<pw and pat[y][x]!=B:
   c=pat[y][x];y+=dy;x+=dx
   return c,0<=y<ph and 0<=x<pw and pat[y][x]==c
  return B,0
 u,nu=a(-1,0);d,nd=a(1,0);l,nl=a(0,-1);r,nr=a(0,1)
 for y0,y1,x0,x1,c in R:
  for y in range(y0,y1+1):
   for x in range(x0,x1+1):
    if g[y][x]!=c:
     for dy,row in enumerate(pat):
      ty=y-cy+dy
      if y0<=ty<=y1:
       for dx,val in enumerate(row):
        tx=x-cx+dx
        if x0<=tx<=x1:h[ty][tx]=c if val==B else val
     if nu:
      for Y1 in range(y0,y):h[Y1][x]=u
     if nd:
      for Y1 in range(y+1,y1+1):h[Y1][x]=d
     if nl:
      for X1 in range(x0,x):h[y][X1]=l
     if nr:
      for X1 in range(x+1,x1+1):h[y][X1]=r
     h[y][x]=cen
 return h
