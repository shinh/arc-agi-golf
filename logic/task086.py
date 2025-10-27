def p(g):
 # expand the plus-shaped frame around asymmetric corners
 h=[r[:]for r in g]
 R=range
 for r in R(len(g)):
  for c in R(len(g[0])):
   if(b:=g[r][c])and g[r][c+1]==g[r+1][c]==b!=g[r+1][c+1]:
    a=1+(g[r][c+3]==b);d=g[r+1][c+1]
    for i in R(r-a,r+2*a+2):
     for j in R(c,c+a+2):h[i][j]=b
    for i in R(r,r+a+2):
     for j in R(c-a,c+2*a+2):h[i][j]=b
     for j in R(c,c+a+2):h[i][j]=d
    for i in R(r+1,r+a+1):
     for j in R(c+1,c+a+1):h[i][j]=b
 return h
