# line
def p(g):
 h=len(g)-1;w=len(g[0])-1
 for y in range(1,h):
  for x in range(1,w):
   c=g[y][x];a=g[y+1][x]==c;a-=g[y-1][x]==c;b=g[y][x+1]==c;b-=g[y][x-1]==c;p,q=x,y
   while c*a*b*(g[y+a][x+b]^c)*(0<q<h>0<p<w):q-=a;p-=b;g[q][p]=g[y+2*a][x+2*b]
 return g
