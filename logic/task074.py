e=enumerate
def p(g):# mirror non9
 for k in 0,1,2,3:
  for i,r in e(g):
   for j,v in e(r):
    if v^9 and (x:=(j,i^31,i^31,i)[k])<30>(y:=(i,j^31,j,j^31)[k]):g[x][y]=v
 return g
