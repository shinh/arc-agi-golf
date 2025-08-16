def p(g):
 # box fill then extend line
 a,c=divmod((s:=sum(g,[])).index(5),10);b,d=divmod(99-s[::-1].index(5),10);dx=dy=0
 for r in g[a+1:b]:r[c+1:d]=[8]*(d-c-1)
 for x in range(c,d+1):
  if g[a][x]<1:y=a;dy=-1;break
  if g[b][x]<1:y=b;dy=1;break
 else:
  for y in range(a,b+1):
   if g[y][c]<1:x=c;dx=-1;break
   if g[y][d]<1:x=d;dx=1;break
 while 0<=y<10 and 0<=x<10:g[y][x]=8;y+=dy;x+=dx
 return g
