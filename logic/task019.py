def p(g):
 # tile grid and add 8s diagonally
 h=len(g);w=len(g[0]);o=[g[y%h]*2 for y in range(h*2)]
 for y in range(h*2):
  for x in range(w*2):
   if g[y%h][x%w]:
    for Y in y-1,y+1:
     for X in x-1,x+1:
      if h*2>Y>-1<X<w*2>o[Y][X]<1:o[Y][X]=8
 return o

