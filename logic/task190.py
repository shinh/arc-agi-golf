def p(g):#ray casting from 2x2 block
 c=max(sum(g,[]))
 for y in range(9):
  for x in range(9):
   if g[y][x]==g[y][x+1]==g[y+1][x]==g[y+1][x+1]==c:a=y;b=x
 for d in-1,1:
  for e in-1,1:
   i=a+d+(d>0);j=b+e+(e>0)
   if-1<i<10 and-1<j<10 and g[i][j]==c:
    while-1<(i:=i+d)<10>(j:=j+e)>-1 and g[i][j]<1:g[i][j]=c
 return g

