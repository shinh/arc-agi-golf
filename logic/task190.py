def p(g):
 n=10
 o=[r[:]for r in g]
 c=next(v for r in g for v in r if v)
 for y in range(9):
  for x in range(9):
   if g[y][x]==c==g[y+1][x]==g[y][x+1]==g[y+1][x+1]:a,b=y,x
 for y in range(10):
  for x in range(10):
   if g[y][x]==c and not(a<=y<a+2 and b<=x<b+2):
    dy=(y>a+1)-(y<a)
    dx=(x>b+1)-(x<b)
    i=y+dy;j=x+dx
    while 0<=i<10 and 0<=j<10 and o[i][j]==0:
     o[i][j]=c;i+=dy;j+=dx
 return o
