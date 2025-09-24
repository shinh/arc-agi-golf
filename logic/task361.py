def p(g):
 # rotate extra cells around biggest solid square
 for k in range(10,0,-1):
  for i in range(11-k):
   for j in range(11-k):
    if min(min(r[j:j+k])for r in g[i:i+k]):
     c=2*i+k-1;d=2*j+k-1
     for y in range(10):
      for x in range(10):
       if (v:=g[y][x])and(1-(i<=y<i+k)*(j<=x<j+k)):
        a,b=2*y-c,2*x-d
        for _ in'000':
         a,b=-b,a
         if 0<=(Y:=(c+a)//2)<10>(X:=(d+b)//2)>=0:g[Y][X]=v
     return g
