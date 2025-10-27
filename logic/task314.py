def p(g):#fill
 for k in range(12):
  r=k//2*3//2
  if(a:=g[r][c:=k%2])==g[r][c+6]!=1:g[r][c+3]=a
  if(b:=g[c][r])==g[c+6][r]!=1:g[c+3][r]=b
 return g
