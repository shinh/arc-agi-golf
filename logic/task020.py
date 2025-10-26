def p(g):
 a=bytes(map(any,g)).find(1)+2
 b=bytes(map(any,zip(*g))).find(1)+2
 for i in range(10):
  for j in range(10):
   if g[i][j]:c=i-a;d=j-b;g[a+c][b-d]=g[a-c][b-d]=g[a-d][b+c]=g[a+d][b-c]=g[i][j]
 return g