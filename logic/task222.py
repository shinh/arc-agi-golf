def p(g):
 t=[]
 for r in range(15):
  for c in range(15):
   if g[r][c]==g[r+1][c]==g[r][c+1]==g[r+1][c+1]>0:t+=g[r][c],
 v=max(t,key=t.count);o=[[0]*16for _ in g]
 for r in range(15):
  for c in range(15):
   if g[r][c]==g[r+1][c]==g[r][c+1]==g[r+1][c+1]==v:
    o[r][c]=o[r][c+1]=o[r+1][c]=o[r+1][c+1]=v
 return o
