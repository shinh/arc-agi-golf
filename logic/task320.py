def p(m,E=enumerate):
 # color bottom half of each filled column 8
 for j,c in E(zip(*m)):
  for k in (S:=[i for i,v in E(c)if v])[-(len(S)//2):]:m[k][j]=8
 return m
