def p(g):#scale+diag
 n=len({*sum(g,[])})-1;z=range(n);sy,sx=(g[0][1]<1)*n,(g[1][0]<1)*n
 g=[[c for c in r for _ in z]for r in g for _ in z]
 for i in z:
  for y in sy+~i,sy+n*2+i:
   for x in sx+~i,sx+n*2+i:
    if(1>g[y][x])*(y|x>-1):g[y][x]=2
 return g
