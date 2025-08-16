# copy motif into rectangular holes and extend rays

def p(g):
 b=g[0][0];h=[r[:]for r in g];v=[[0]*30 for _ in g];R=[]
 for y in range(30):
  for x in range(30):
   if g[y][x]!=b and not v[y][x]:
    c=g[y][x];q=[(y,x)];v[y][x]=1
    for i,j in q:
     for Y,X in((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
      if 0<=Y<30 and 0<=X<30 and g[Y][X]==c and not v[Y][X]:v[Y][X]=1;q.append((Y,X))
    ys,xs=zip(*q);y0=min(ys);y1=max(ys);x0=min(xs);x1=max(xs);n=len(q)
    if n>20 and(y1-y0+1)*(x1-x0+1)-n<5:R+=[(y0,y1,x0,x1,c)]
 P=[(y,x)for y in range(30)for x in range(30)if g[y][x]!=b and not any(y0<=y<=y1 and x0<=x<=x1 for y0,y1,x0,x1,_ in R)]
 for y,x in P:h[y][x]=b
 ys,xs=zip(*P);my,My=min(ys),max(ys);mx,Mx=min(xs),max(xs)
 A=[[b]*(Mx-mx+1)for _ in range(My-my+1)]
 for y,x in P:A[y-my][x-mx]=g[y][x]
 H=len(A);W=len(A[0]);cy=H//2;cx=W//2;cen=A[cy][cx];C=[]
 for dy,dx in((-1,0),(0,1),(1,0),(0,-1)):
  y,x=cy+dy,cx+dx;c=b;f=0
  if 0<=y<H and 0<=x<W and A[y][x]!=b:
   c=A[y][x];y+=dy;x+=dx;f=0<=y<H and 0<=x<W and A[y][x]==c
  C+=[c,f]
 for y0,y1,x0,x1,c in R:
  for y in range(y0,y1+1):
   for x in range(x0,x1+1):
    if g[y][x]!=c:
     for dy,r in enumerate(A):
      ty=y-cy+dy
      if y0<=ty<=y1:
       u=h[ty]
       for dx,v in enumerate(r):
        tx=x-cx+dx
        if x0<=tx<=x1:u[tx]=c if v==b else v
     for i,(dy,dx) in enumerate(((-1,0),(0,1),(1,0),(0,-1))):
      if C[i*2+1]:
       Y=y+dy;X=x+dx
       while y0<=Y<=y1 and x0<=X<=x1:h[Y][X]=C[i*2];Y+=dy;X+=dx
     h[y][x]=cen
 return h
