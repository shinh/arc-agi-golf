def p(g,E=enumerate):# ring5
 for r,R in E(g):
  for c,C in E(R):
   if C>4:
    for L in g[r-1:r+2]:L[c-1:c+2]=[1]*3;R[c]=5
 return g
