def p(g):#arch->4
 for r,b in zip(g,g[1:]):
  for j in range(1,len(r)-1):g[-1][j]|=4*(b[j-1]==b[j+1]==r[j]>b[j])
 return g
