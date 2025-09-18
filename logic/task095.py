def p(g,E=enumerate):#ring
 for r,R in E(g):
  for c,C in E(R):
   for L in g[r-1:r+2]*(C>4):L[c-1:c+2]=1,1,1;R[c]=5
 return g
