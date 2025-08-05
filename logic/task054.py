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
 cy=len(pat)//2;cx=len(pat[0])//2;cen=pat[cy][cx];C=[]
 for _ in range(4):
  y,x=len(pat)//2-1,len(pat[0])//2
  if y>=0 and pat[y][x]!=B:
   c=pat[y][x];y-=1;C+=[c,y>=0 and pat[y][x]==c]
  else:C+=[B,0]
  pat=[list(r)for r in zip(*pat[::-1])]
 cy=len(pat)//2;cx=len(pat[0])//2
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
     for _ in range(4):
      col,fl=C[0],C[1]
      if fl:
       for Y1 in range(y0,y):h[Y1][x]=col
      h=[list(r)for r in zip(*h[::-1])]
      y,x=x,Y-1-y
      y0,y1,x0,x1=x0,x1,Y-1-y1,Y-1-y0
      C=C[2:]+C[:2]
     h[y][x]=cen
 return h
