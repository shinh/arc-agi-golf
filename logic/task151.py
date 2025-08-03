def p(g):
 h=len(g);w=len(g[0])
 for y in range(1,h-1):
  for x in range(1,w-1):
   a=g[y][x-1];b=g[y][x+1];c=g[y-1][x];d=g[y+1][x]
   if a==b!=0 and c==d!=0 and a!=c and g[y][x]in(a,c):
    e=g[y][x]
    for i in-1,0,1:
     for j in-1,0,1:g[y+i][x+j]=4
    g[y][x]=e;return g
 return g
