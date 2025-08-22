# fill rows/cols of zeros with 3
def p(g):
 r=eval(str(g));q=range(1,len(g)-1)
 for i in q:
  for j in q:
   if any(g[i][1:-1])*any(g[k][j]for k in q)<1:r[i][j]=3
 return r

