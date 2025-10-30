def p(g):
 # extend arms
 m=max(c.count(3)for c in zip(*g))
 for i in range(10):
  for j in range(10):
   if 3==g[i][j]:
    for s in-1,1:
     if-1<(a:=i+m)<10 and-1<(b:=j+s*m)<10 and 3==g[a][b]:
      if-1<(a:=i-m)<10 and-1<(b:=j+2*s*m)<10:g[a][b]=8
      if-1<(a:=i+2*m)<10 and-1<(b:=j-s*m)<10:g[a][b]=8
 return g
