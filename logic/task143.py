def p(g):
 G=[r[:]for r in g];O=[]
 for y in range(10):
  for x in range(10):
   c=G[y][x]
   if c:
    q=[(y,x)];G[y][x]=0;o={(y,x)}
    for i,j in q:
     for a,b in((1,0),(-1,0),(0,1),(0,-1)):
      A=i+a;B=j+b
      if 0<=A<10 and 0<=B<10 and G[A][B]==c:G[A][B]=0;q+=[(A,B)];o|={(A,B)}
    Y,X=zip(*o);sy=min(Y);sx=min(X);ey=max(Y);ex=max(X);O+=((c,o,sy,sx,ey,ex,{(y-sy,x-sx)for y,x in o}),)
 m=0
 for t in O:
  c,o,sy,sx,ey,ex,_=t
  if len(o)==ey-sy+ex-sx+1 and sy*sx*(9-ey)*(9-ex)==0 and len({g[i][j]for i in range(sy,ey+1)for j in range(sx,ex+1)}-{c})==2 and len(o)>m:L=t;m=len(o)
 c,o,sy,sx,ey,ex,sh=L
 for t in O:
  if t[1]!=o and all(sy<=y<=ey and sx<=x<=ex for y,x in t[1]):S=t;break
 sh=S[6]
 for t in O:
  if t[6]==sh and t[1]!=S[1]:
   for y,x in t[1]:g[y][x]=c
   break
 return g
