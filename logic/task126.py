def p(g):#arch->4
 for a,b in zip(g[1:],g):
  for j in range(1,len(a)-1):
   if 0==a[j]<a[j-1]==a[j+1]==b[j]:g[-1][j]=4
 return g
