def p(g,E=enumerate):# color nbrs
 for r,R in E(g):
  for c,C in E(R):
   for i in(-1,1)*(268>>C&1):H=g[r+i];H[c]=R[c+i]=H[c+i]=H[c-i]=C*5%9
 return g
