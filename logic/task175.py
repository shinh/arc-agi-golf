def p(g):
 # mirror diag & fill zeros with most common color
 n=range(21);a=sum(g,[]);m=max(set(a)-{0},key=a.count);k=a[0]
 for i in n:
  for j in n:g[i][j]=g[j][i]=g[i][j] or g[j][i] or m
  g[i][i]=k
 return g

