def p(g,Y=range):
 Q=[r[:]for r in g]
 for c in Y(1,10):
  b=[(i,j)for i in Y(len(g))for j in Y(len(g[0]))if g[i][j]==c]
  for i in Y(len(b)):
   for j in Y(i+1,len(b)):
    M,K=b[i]
    Z,C=b[j]
    if M==Z:
     for x in Y(min(K,C),max(K,C)+1):Q[M][x]=c
    elif K==C:
     for y in Y(min(M,Z),max(M,Z)+1):Q[y][K]=c
 return Q