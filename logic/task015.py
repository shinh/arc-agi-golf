# color diagonals of 2 with 4 and orthogonals of 1 with 7
E=enumerate
def p(g):
 for r,row in E(g):
  for c,v in E(row):
   for t in 1,-1:
    if v==2:g[r+t][c+t]=g[r+t][c-t]=4
    if v==1:g[r][c+t]=g[r+t][c]=7
 return g
