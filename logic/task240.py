def p(g):
 for i in range(1,9,2):
  for j in range(1,9,2):g[i][j]=g[i][~j]=g[~i][j]=g[~i][~j]=g[~i][j]or g[~i][~j]or g[i][j]or g[i][~j]
  for j in range(i+2,17-i,2):g[i][j]=g[~i][j]=g[j][i]=g[j][~i]=g[i][i+2]
 return g
