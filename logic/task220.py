def p(g,E=enumerate):
# color neighbors
 d={8:4,2:1,3:6}
 for r,R in E(g):
  for c,C in E(R):
   for i in-1,0,1:
    for j in-1,0,1:
     if C and(i|j):
      try:g[r+i][c+j]=d[C]
      except:0
 return g
