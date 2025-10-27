def p(g):
 n=len(g)
 for i in range(1,n-1):
  for j in range(1,n-1):
   if 0<g[i][j]==g[i-1][j-1]==g[i-1][j+1]==g[i+1][j-1]==g[i+1][j+1]:y,x=i,j
 for i in range(n):
  for j in range(n):
   if(v:=g[i][j]):g[i][2*x-j]=g[2*y-i][j]=g[2*y-i][2*x-j]=v
 return g
