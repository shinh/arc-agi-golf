def p(g):
 o=[[0]*9for _ in range(9)]
 for y in range(len(g)-2):
  for x in range(len(g[0])-2):
   a=[]
   v=0
   for d in range(9):
    c=g[y+d//3][x+d%3]
    a.append(c)
    v+=(d+2)*(c!=5)
   if all(a):
    p={
     10:0,15:3,14:6,
     21:27,0:30,27:33,
     22:54,33:57,26:60,
    }[v]
    for d in range(9):
     o[p//9+d//3][p%9+d%3]=g[y+d//3][x+d%3]
 return o

