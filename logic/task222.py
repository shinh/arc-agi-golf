def p(g):
 h=[0]*10
 for r in range(15):
  for c in range(15):
   k=g[r][c]
   if k and k==g[r+1][c]==g[r][c+1]==g[r+1][c+1]:h[k]+=1
 v=h.index(max(h));o=[[0]*16for _ in g]
 for r in range(15):
  for c in range(15):
   if g[r][c]==v==g[r+1][c]==g[r][c+1]==g[r+1][c+1]:
    o[r][c]=o[r][c+1]=o[r+1][c]=o[r+1][c+1]=v
 return o