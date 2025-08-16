def p(g):
 #bounce from bottom left
 m=len(g[0])-1
 for k in range(len(g)):
  g[~k][m-abs(k%(m*2)-m)]=1
 return g
