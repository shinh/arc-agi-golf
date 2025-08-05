def p(g):
 h=len(g);w=len(g[0])
 a=h;b=0;c=w;d=0
 for y,r in enumerate(g):
  for x,v in enumerate(r):
   if v==5:
    if y<a:a=y
    if y>b:b=y
    if x<c:c=x
    if x>d:d=x
 for y in range(a+1,b):
  for x in range(c+1,d):g[y][x]=8
 x=y=0;dy=dx=0
 for i in range(c,d+1):
  if g[a][i]==0:y=a;x=i;dy=-1;break
  if g[b][i]==0:y=b;x=i;dy=1;break
 if dy==0:
  for i in range(a,b+1):
   if g[i][c]==0:y=i;x=c;dx=-1;break
   if g[i][d]==0:y=i;x=d;dx=1;break
 while 0<=y<h and 0<=x<w:
  g[y][x]=8;y+=dy;x+=dx
 return g
