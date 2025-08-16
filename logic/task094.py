L=len;R=range
# cross 16 ones with 6

def p(g):
 for r in R(L(g)-4):
  for c in R(L(g[0])-4):
   if sum(g[r+i][c+j]==1for i in R(5)for j in R(5))==16:
    for q in g:q[c+2]=q[c+2]==1 or 6
    g[r+2]=[q==1 or 6 for q in g[r+2]]
 return g
