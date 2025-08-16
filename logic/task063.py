# fill rows/cols of zeros with 3
def p(g):
 q=range;r=[*map(list,g)];t=q(1,len(g)-1)
 for i in t:
  for j in t:
   if sum(g[i][1:-1])*sum(g[k][j]for k in t)<1:r[i][j]=3
 return r

