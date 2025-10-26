def p(g):
 R=range(15);t=[g[r][c]for r in R for c in R if g[r][c]==g[r+1][c]==g[r][c+1]==g[r+1][c+1]>0]
 v=max(t,key=t.count);o=[[0]*16for _ in g]
 for r in R:
  for c in R:
   if g[r][c]==g[r+1][c]==g[r][c+1]==g[r+1][c+1]==v:
    o[r][c]=o[r][c+1]=o[r+1][c]=o[r+1][c+1]=v
 return o
