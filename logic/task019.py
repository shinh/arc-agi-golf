def p(g):
 # tile grid and add 8s diagonally
 h=len(g);w=len(g[0]);H=h*2;W=w*2;r=range;o=[g[y%h]*2 for y in r(H)]
 for y in r(H):
  for x in r(W):
   if g[y%h][x%w]:
    for Y in y-1,y+1:
     for X in x-1,x+1:
      if H>Y>=0<=X<W and o[Y][X]<1:o[Y][X]=8
 return o

