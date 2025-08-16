def p(g):#scale&draw diagonals
 n=len({*sum(g,[])})-1
 sy,sx=(g[0][1]<1)*n,(g[1][0]<1)*n
 g=[[c for c in r for _ in[0]*n]for r in g for _ in[0]*n]
 for i in range(n):
  for y in sy-i-1,sy+n+n+i:
   for x in sx-i-1,sx+n+n+i:
    if g[y:y+1]and g[y][x:x+1]and g[y][x]<1:g[y][x]=2
 return g
