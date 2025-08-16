def p(m,O=range):
 # color bottom half of each filled column 8
 for j in O(len(m[0])):
  for k in (S:=[i for i in O(len(m))if m[i][j]])[-(len(S)//2):]:m[k][j]=8
 return m
