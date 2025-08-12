# 104
def p(g):
 for _ in range(4):
  while set(g[0])=={0}:g=g[1:]
  g=[*zip(*g[::-1])]
 q=[(i//3,j//3)for i in range(0,9,3)for j in range(0,9,3)if g[i][j]]
 o=[[0]*9 for _ in range(9)]
 for x,y in q:
  for u,v in q:o[x*3+u][y*3+v]=5
 return o
