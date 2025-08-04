def p(g):
 n=len(g);h=[r[:]for r in g]
 for i in range(n):
  for j in range(n):
   if h[i][j]:g[j][i]=h[i][j]
 c=g[0][0]
 for i in range(n):g[i][i]=c
 z={(i,j)for i in range(n)for j in range(n)if g[i][j]==0}
 if z:
  s={(x,y)for i,j in z for x,y in((i+1,j),(i-1,j),(i,j+1),(i,j-1))if 0<=x<n and 0<=y<n and g[x][y]}
  if s:
   v=[g[i][j]for i,j in s];f=max(set(v),key=lambda k:(v.count(k),k))
   for i,j in z:g[i][j]=f
 return g
