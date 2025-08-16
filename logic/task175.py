def p(g):
 # mirror diag & fill zeros
 n=range(21)
 for i in n:
  for j in n:g[i][j]=g[j][i]=g[i][j]or g[j][i];g[i][i]=g[0][0]
 z=[(i,j)for i in n for j in n if g[i][j]<1];s={(x,y)for i,j in z for x,y in((i+1,j),(i-1,j),(i,j+1),(i,j-1))if 0<=x<21>y>=0<g[x][y]}
 if v:=[g[i][j]for i,j in s]:
  f=max(v,key=v.count)
  for i,j in z:g[i][j]=f
 return g

