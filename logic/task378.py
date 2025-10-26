# line
def p(g):
 for y in range(1,len(g)-1):
  for x in range(1,len(g[0])-1):
   c=g[y][x];a=(g[y+1][x]==c)-(g[y-1][x]==c);b=(g[y][x+1]==c)-(g[y][x-1]==c);p,q=x,y
   while c*a*b*(g[y+a][x+b]^c)and-1<(q:=q-a)<len(g)and-1<(p:=p-b)<len(g[0]):g[q][p]=g[y+a+a][x+b+b]
 return g
