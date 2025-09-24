def p(g,E=enumerate):
# color neighbors
 for r,R in E(g):
  for c,C in E(R):
   if 268>>C&1:
    for i in-1,1:
     H=g[r+i];H[c]=R[c+i]=H[c+i]=H[c-i]=C*5%9
 return g
