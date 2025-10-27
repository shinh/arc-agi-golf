def p(g,E=enumerate):#paint nb
 for r,R in E(g):
  for c,C in E(R):
   for i in(-1,1)*(1<C%6<4):R[c+i]=k=C*5%9;g[r+i][c-1:c+2]=[k]*3
 return g
