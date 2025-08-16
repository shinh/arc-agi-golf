# reflect diagonal from 8s off 2s
def p(g):
 z=lambda y,x:(-1<x<12>y>-1)and g[y][x]
 for a in 1,-1:
  for b in 1,-1:
   f=0;n=[r[:]for r in g]
   for i in range(12):
    for x in range(12):
     y=i
     if g[y][x]&z(y-a,x-b)&8:
      y+=a;x+=b
      while-1<x<12>y>-1:
       if g[y][x]==2:
        f=1;y-=a;x-=b
        z(y+a-1,x+b)&z(y+a+1,x+b)&2 and(b:=-b)or(a:=-a)
        continue
       if g[y][x]:break
       n[y][x]=3;y+=a;x+=b
   f and(g:=n)
 return g
