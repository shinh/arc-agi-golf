# color diagonals of 2 with 4 and orthogonals of 1 with 7
e=enumerate
def p(g):
 for r,R in e(g):
  for c,v in e(R):
   if-1<(b:=v-1)<2:
    for t in-1,1:g[r+b*t][c+t]=g[r+t][c-b*t]=7-3*b
 return g
