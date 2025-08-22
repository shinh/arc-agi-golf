def p(g):# anchor then pour down
 r=range;a=3,3,2,2,2,2,1,1,1,0;b=6,0,5,4,2,1,4,3,2,3;d=1,0,0,-1,0,0,1
 for y in r(17):
  for x in r(14):
   if(c:=g[y+3][x+6])and all(g[y+a[i]][x+b[i]]==c for i in r(10)):
    for i in r(7):
     X=x+6-i;Y=y+3+d[i];t=next((R[X]for R in g[Y:]if R[X]),0)
     for R in g[Y:]:R[X]=t
    return g
