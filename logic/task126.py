def p(g):#arch->4
 for r,b in zip(g,g[1:]):
  for j in range(1,len(r)-1):
   if b[j-1]==b[j+1]==r[j]>b[j]<1:g[-1][j]=4
 return g
