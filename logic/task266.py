def p(g):
 # fill diagonals around 2
 i=sum(g,[]).index(2);g[x:=i//5][y:=i%5]=0
 for v in 3,8,6,7:
  if 3>(X:=x-1+2*(v>6))>-1<(Y:=y-1+2*(5<v<8))<5:g[X][Y]=v
 return g

