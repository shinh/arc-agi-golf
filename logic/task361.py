def p(g):
 # rotate non-square cells around center of largest solid square
 for k in range(10,0,-1):
  for i in range(11-k):
   for j in range(11-k):
    if all(min(g[i+y][j:j+k])for y in range(k)):
     c=i+k/2-.5;d=j+k/2-.5
     for y in range(10):
      for x in range(10):
       if (v:=g[y][x])*(i<=y<i+k)*(j<=x<j+k)<v:
        a=y-c;b=x-d
        for _ in'000':
         a,b=-b,a;y2=round(c+a);x2=round(d+b)
         if 0<=y2<10>x2>=0:g[y2][x2]=v
     return g
