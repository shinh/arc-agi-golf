def p(g):
 h=len(g);w=len(g[0])
 for y in range(h):
  for x in range(w):
   if g[y][x]==5:
    for s in(3,4,5):
     if y+s<=h and x+s<=w and all(g[y][x+k]==g[y+s-1][x+k]==g[y+k][x]==g[y+k][x+s-1]==5 for k in range(s)):
      c=s+3
      for i in range(1,s-1):
       for j in range(1,s-1):g[y+i][x+j]=c
 return g
