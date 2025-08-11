def p(g):
 for y in range(len(g)):
  for x in range(len(g[0])):
   c=g[y][x]
   if c:g[y%10][x%10]=c
 for y in range(len(g)):
  for x in range(len(g[0])):
   g[y][x]=g[y%10][x%10]
 return g
