def p(g):
 # fill holes w/|size-4|
 def d(i,j):
  if 0<=i<10>j>=0==g[i][j]:
   g[i][j]=1;return[(i,j),*d(i+1,j),*d(i-1,j),*d(i,j+1),*d(i,j-1)]
  return[]
 for k in range(100):
  for i,j in(s:=d(k//10,k%10)):g[i][j]=abs(len(s)-4)
 return g
