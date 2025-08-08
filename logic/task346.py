def p(g):
 for i in range(len(g)):
  for j in range(len(g[0])-1):
   b=g[i][j]
   a=g[i-1][j]
   if a*all(a==g[i+di][j+dj]for di in(-1,0,1) for dj in(-1,0,1) if di|dj):
    return[[b]]
