def p(g):
 def d(i,j):
  if not(-1<i<10>j>-1)or g[i][j]:return[]
  g[i][j]=1;return[(i,j)]+[e for a,b in((1,0),(-1,0),(0,1),(0,-1))for e in d(i+a,j+b)]
 for i in range(10):
  for j in range(10):
   if g[i][j]==0:
    s=d(i,j)
    for a,b in s:g[a][b]=abs(len(s)-4)
 return g
