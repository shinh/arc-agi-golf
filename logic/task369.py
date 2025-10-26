def p(g):
 def f(i,j,a,d):
  if g[i][j]-a:return 0
  g[i][j]=d
  return 1+(i and f(i-1,j,a,d))+(i<9 and f(i+1,j,a,d))+(j and f(i,j-1,a,d))+(j<9 and f(i,j+1,a,d))
 for i in range(10):
  for j in range(10):f(i,j,9,4-f(i,j,0,9))
 return g