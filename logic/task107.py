def p(g):
 sx=g[1][0]<1
 sy=g[0][1]<1
 n=len({*sum(g,[])})-1
 g=[[c for c in r for _ in[0]*n]for r in g for _ in[0]*n]
 sx*=n;sy*=n;t=2*n
 for i in range(n):
  for y in sy-i-1,sy+t+i:
   for x in sx-i-1,sx+t+i:
    if g[y:y+1]and g[y][x:x+1]and g[y][x]<1:g[y][x]=2
 return g
