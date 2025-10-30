def p(g):#fill
 for k in range(12):
  if(a:=g[(r:=k//2*3>>1)][c:=k&1])==g[r][c+6]!=1:g[r][c+3]=a
  if(b:=g[c][r])==g[c+6][r]!=1:g[c+3][r]=b
 return g
