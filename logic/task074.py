R=range(30)
def p(g):# mirror non9
 for k in R[:4]:
  for i in R:
   for j in R:
    if (v:=g[i][j])^9 and (x:=(j,i^31,i^31,i)[k])<30>(y:=(i,j^31,j,j^31)[k]):g[x][y]=v
 return g
