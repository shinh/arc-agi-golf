# line
def p(g):
 h=len(g);w=len(g[0])
 for y in range(1,h-1):
  for x in range(1,w-1):
   c=g[y][x];a=(g[y+1][x]==c)-(g[y-1][x]==c);b=(g[y][x+1]==c)-(g[y][x-1]==c);p,q=x,y
   while c*a*b*(g[y+a][x+b]^c)and-1<(q:=q-a)<h and-1<(p:=p-b)<w:g[q][p]=g[y+a+a][x+b+b]
 return g
