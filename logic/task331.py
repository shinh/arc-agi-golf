def p(g,E=enumerate):
 # mark neighbors of 1
 for r,R in E(g):
  for c,C in E(R):
   if C%2:
    if r:g[r-1][c]=2
    if r-9:g[r+1][c]=8
    if c:R[c-1]=7
    if c-9:R[c+1]=6
 return g
