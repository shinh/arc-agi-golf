def p(g):#ray casting from 2x2 block
 c=max(sum(g,[]))
 for y in range(9):
  for x in range(9):
   if g[y][x:x+2]==g[y+1][x:x+2]==[c]*2:a=y;b=x
 for d in-1,1:
  for e in-1,1:
   i,j=a+d+(d>0),b+e+(e>0)
   if-1<i<10>j>-1<g[i][j]==c:
    while-1<(i:=i+d)<10>(j:=j+e)>-1<g[i][j]<1:g[i][j]=c
 return g

