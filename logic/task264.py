def p(g):
 o=[[0]*9for _ in[0]*9]
 k=[10,15,14,21,0,27,22,33,26]
 for y in range(len(g)-2):
  for x in range(len(g[0])-2):
   v=0
   for d in range(9):
    c=g[y+d//3][x+d%3]
    if c<1:break
    v+=(d+2)*(c!=5)
   else:
    c=k.index(v)
    for d in range(9):
     o[c//3*3+d//3][c%3*3+d%3]=g[y+d//3][x+d%3]
 return o

