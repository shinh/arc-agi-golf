def p(g):
 n=len(g)
 o=[r[:] for r in g]
 c=next(v for r in g for v in r if v)
 for y in range(n-1):
  for x in range(n-1):
   if g[y][x]==c==g[y+1][x]==g[y][x+1]==g[y+1][x+1]:a,b=y,x
 for y in range(n):
  for x in range(n):
   if g[y][x]==c and not(a<=y<a+2 and b<=x<b+2):
    dy=(y>a+1)-(y<a)
    dx=(x>b+1)-(x<b)
    i=y+dy;j=x+dx
    while 0<=i<n and 0<=j<n and o[i][j]==0:
     o[i][j]=c;i+=dy;j+=dx
 return o
