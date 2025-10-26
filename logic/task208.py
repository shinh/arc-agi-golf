def p(g):
 f=sum(g,[])
 k=min({*f}-{0},key=f.count)
 x=f.index(k)
 y=440-f[::-1].index(k)
 h=y//21-x//21-1
 w=y%21-x%21-1
 for i in range(22-h):
  for j in range(22-w):
   if not sum(sum(r[j:j+w])for r in g[i:i+h]):
    for r in g[i-1:i+h+1]:r[j-1]=r[j+w]=k
    g[i-1][j-1:j+w+1]=g[i+h][j-1:j+w+1]=[k]*(w+2)
 return g