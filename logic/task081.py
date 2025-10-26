def p(g):
 for c in range(36):
  i=c//6;j=c%6
  s=g[i][j:j+2]+g[i+1][j:j+2]
  if sum(s)>23:k=s.index(0);g[i+k//2][j+k%2]=1
 return g