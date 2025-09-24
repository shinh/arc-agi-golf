def p(g):# fill diagonals around 2
 i=sum(g,[]).index(2);g[i//5][i%5]=0
 for v in 3,8,6,7:
  if 3>(X:=i//5+(v>6)*2-1)>-1<(Y:=i%5+(v&4)//2-1)<5:g[X][Y]=v
 return g
