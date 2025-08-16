# copy motif into rectangular holes and extend rays

def p(g):
 b=g[0][0];h=[r[:]for r in g];o=[r[:]for r in g];R=[];B=range(30);d=((1,0),(-1,0),(0,1),(0,-1))
 for y in B:
  for x in B:
   if g[y][x]!=b:
    c=g[y][x];q=[(y,x)];g[y][x]=b
    for i,j in q:
     for dy,dx in d:
      Y=i+dy;X=j+dx
      if 0<=Y<30 and 0<=X<30 and g[Y][X]==c:g[Y][X]=b;q+=[(Y,X)]
    ys,xs=zip(*q);y0,y1,x0,x1=min(ys),max(ys),min(xs),max(xs);n=len(q)
    if n>20 and(y1-y0+1)*(x1-x0+1)-n<5:R+=[(y0,y1,x0,x1,c)]
 P=[(y,x)for y in B for x in B if o[y][x]!=b and not any(y0<=y<=y1 and x0<=x<=x1 for y0,y1,x0,x1,_ in R)]
 ys,xs=zip(*P);my,My,mx,Mx=min(ys),max(ys),min(xs),max(xs)
 A=[r[mx:Mx+1]for r in o[my:My+1]]
 for y,x in P:h[y][x]=b
 H=len(A);W=len(A[0]);cy,cx=H//2,W//2;cen=A[cy][cx];C=[]
 for dy,dx in d:
  y,x=cy+dy,cx+dx;c=b;f=0
  if 0<=y<H and 0<=x<W and A[y][x]!=b:c=A[y][x];y+=dy;x+=dx;f=0<=y<H and 0<=x<W and A[y][x]==c
  C+=[(c,f)]
 for y0,y1,x0,x1,c in R:
  for y in range(y0,y1+1):
   for x in range(x0,x1+1):
    if o[y][x]!=c:
     for dy,r in enumerate(A):
      ty=y-cy+dy
      if y0<=ty<=y1:
       u=h[ty]
       for dx,v in enumerate(r):
        tx=x-cx+dx
        if x0<=tx<=x1:u[tx]=c if v==b else v
     for (k,f),(dy,dx) in zip(C,d):
      if f:
       Y=y+dy;X=x+dx
       while y0<=Y<=y1 and x0<=X<=x1:h[Y][X]=k;Y+=dy;X+=dx
     h[y][x]=cen
 return h

