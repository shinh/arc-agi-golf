def p(g):
 for y,r in enumerate(g):
  for x,v in enumerate(r):
   if v==8:c=x
   if v==2:s=y
 o=[[0]*6 for _ in g]
 for y in range(6):
  if y==s:o[y]=[2]*6;o[y][c]=4
  else:o[y][c]=8
 return o
