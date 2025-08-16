def p(g):
 i=sum(g,[]).index(2);g[x:=i//5][y:=i%5]=0
 for v,X,Y in((3,x-1,y-1),(8,x+1,y-1),(6,x-1,y+1),(7,x+1,y+1)):
  if 3>X>-1<Y<5:g[X][Y]=v
 return g