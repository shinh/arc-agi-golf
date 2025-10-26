def p(g):
 # expand the plus-shaped frame around asymmetric corners
 h=[r[:]for r in g]
 for r in range(len(g)):
  for c in range(len(g[0])):
   b=g[r][c]
   if b and g[r][c+1]==g[r+1][c]==b!=g[r+1][c+1]:
    a=1+(g[r][c+3]==b)
    for i in range(r-a,r+2*a+2):
     for j in range(c,c+a+2):h[i][j]=b
    for i in range(r,r+a+2):
     for j in range(c-a,c+2*a+2):h[i][j]=b
    d=g[r+1][c+1]
    for i in range(r,r+a+2):
     for j in range(c,c+a+2):h[i][j]=d
    for i in range(r+1,r+a+1):
     for j in range(c+1,c+a+1):h[i][j]=b
 return h
