def p(g):
 for i in 1,3,5,7:
  for j in 1,3,5,7:g[i][j]=g[i][18-j]=g[18-i][j]=g[18-i][18-j]=g[i][j]or g[i][18-j]or g[18-i][j]or g[18-i][18-j]
 for i in 1,3,5,7:
  for j in range(i+2,17-i,2):g[i][j]=g[18-i][j]=g[j][i]=g[j][18-i]=g[i][i+2]
 return g