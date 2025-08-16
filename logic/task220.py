def p(g,E=enumerate):
# color neighbors
 d={8:4,2:1,3:6};N=-1,0,1;X=[*map(list,g)]
 for r,R in E(X):
  for c,C in E(R):
   for i in N:
    for j in N:
     if C and(i|j):
      try:X[r+i][c+j]=d[C]
      except:0
 return X
