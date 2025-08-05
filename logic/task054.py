def p(g):
 h=[r[:]for r in g];Y=len(g);X=len(g[0]);B=g[0][0];v=[[0]*X for _ in g];R=[]
 for y in range(Y):
  for x in range(X):
   if g[y][x]!=B and not v[y][x]:
    c=g[y][x];q=[(y,x)];v[y][x]=1;y0=y1=y;x0=x1=x
    for Y0,X0 in q:
     y0=min(y0,Y0);y1=max(y1,Y0);x0=min(x0,X0);x1=max(x1,X0)
     for Y2,X2 in((Y0+1,X0),(Y0-1,X0),(Y0,X0+1),(Y0,X0-1)):
      if 0<=Y2<Y and 0<=X2<X and g[Y2][X2]==c and not v[Y2][X2]:v[Y2][X2]=1;q+=(Y2,X2),
    n=len(q)
    if n>20 and (y1-y0+1)*(x1-x0+1)-n<5:R+=(y0,y1,x0,x1,c),
 P=[];my=Y;mx=X;My=0;Mx=0
 for y in range(Y):
  for x in range(X):
   if g[y][x]!=B and not any(y0<=y<=y1 and x0<=x<=x1 for y0,y1,x0,x1,_ in R):
    P+=(y,x),;h[y][x]=B
    my=min(my,y);My=max(My,y);mx=min(mx,x);Mx=max(Mx,x)
 pat=[[B]*(Mx-mx+1)for _ in range(My-my+1)]
 for y,x in P:pat[y-my][x-mx]=g[y][x]
 ph=len(pat);pw=len(pat[0]);cy=ph//2;cx=pw//2
 def a(dy,dx):
  y,x=cy+dy,cx+dx
  if 0<=y<ph and 0<=x<pw and pat[y][x]!=B and 0<=y+dy<ph and 0<=x+dx<pw and pat[y+dy][x+dx]==pat[y][x]:return pat[y][x]
  return B
 u=a(-1,0);d=a(1,0);l=a(0,-1);r=a(0,1)
 for y0,y1,x0,x1,c in R:
  for y in range(y0,y1+1):
   for x in range(x0,x1+1):
    if g[y][x]!=c:
     for dy,row in enumerate(pat):
      ty=y-cy+dy
      if y0<=ty<=y1:
       for dx,val in enumerate(row):
        tx=x-cx+dx
        if x0<=tx<=x1:h[ty][tx]=val if val!=B else c
     for C,Ri in ((u,range(y0,y)),(d,range(y+1,y1+1))):
      if C!=B:
       for Y1 in Ri:h[Y1][x]=C
     for C,Ri in ((l,range(x0,x)),(r,range(x+1,x1+1))):
      if C!=B:
       for X1 in Ri:h[y][X1]=C
 return h
