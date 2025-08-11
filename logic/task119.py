def p(g):
 z=lambda y,x:g[y][x]if-1<x<12>y>-1 else 0
 for a in 1,-1:
  for b in 1,-1:
   n=[*map(list,g)];f=0
   for i in range(12):
    for x in range(12):
     y=i
     if g[y][x]&z(y-a,x-b)==8:
      y+=a;x+=b
      while-1<x<12>y>-1:
       if g[y][x]==2:
        f=1;y-=a;x-=b
        if z(y+a-1,x+b)&z(y+a+1,x+b)==2:b=-b
        else:a=-a
        continue
       if g[y][x]:break
       n[y][x]=3;y+=a;x+=b
   g=[g,n][f]
 return g