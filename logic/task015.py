# color diagonals of 2 with 4 and orthogonals of 1 with 7
E=enumerate
def p(g):
 for r,row in E(g):
  for c,v in E(row):
   if 0<v<3:
    b=v>1
    for t in-1,1:g[r+b*t][c+t]=g[r+t][c-b*t]=7-3*b
 return g
