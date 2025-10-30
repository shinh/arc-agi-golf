def p(g):
 a=sum(g,[])
 k=min(a,key=a.count)
 i=a.index(k)
 w=g[i//21].count(k)-2
 h=a.count(k)//2-w-2
 for i in range(22-h):
  for j in range(22-w):
   if not sum(sum(r[j:j+w])for r in g[i:i+h]):
    for r in g[i-1:i+h+1]:r[j-1]=r[j+w]=k
    g[i-1][j-1:j+w+1]=g[i+h][j-1:j+w+1]=[k]*(w+2)
 return g