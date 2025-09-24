def p(g):# anchor then pour down
 r=range
 for y in r(17):
  for x in r(14):
   if(c:=g[y+3][x+6])*all(g[y+i//7][x+i%7]==c for i in(27,21,19,18,16,15,11,10,9,3)):
    for i in r(7):
     X=x+6-i;Y=y+3+(i%6<1)-(i==3);t=0
     for R in g[Y:]:t=t or R[X]
     for R in g[Y:]:R[X]=t
    return g
