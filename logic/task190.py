def p(g):#extend rays
 any((a:=y,b:=x,c)for y in range(9)for x in range(9)if(c:=g[y][x])==g[y+1][x]==g[y][x+1]==g[y+1][x+1]>0)
 for y in range(10):
  for x in range(10):
   if g[y][x]==c and(y-a>>1 or x-b>>1):
    d=(y>a+1)-(y<a);e=(x>b+1)-(x<b);i=y;j=x
    while-1<(i:=i+d)<10>(j:=j+e)>-1 and g[i][j]<1:g[i][j]=c
 return g
