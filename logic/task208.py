def p(g):
 n=21
 f=sum(g,[])
 k=min({*f}-{0},key=f.count)
 x=f.index(k)
 y=440-f[::-1].index(k)
 h=y//n-x//n-1
 w=y%n-x%n-1
 for i in range(n-h+1):
  for j in range(n-w+1):
   if sum(sum(r[j:j+w])for r in g[i:i+h])<1:
    for r in range(i-1,i+h+1):g[r][j-1]=g[r][j+w]=k
    for c in range(j-1,j+w+1):g[i-1][c]=g[i+h][c]=k
 return g