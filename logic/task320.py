def p(g,Y=range):
 h,w=len(g),len(g[0])
 g=[[2 if C>0 else 0 for C in R]for R in g]
 for c in Y(w):
  C=[g[r][c]for r in Y(h)][::-1]
  r=sum(C)//2//2
  for i in Y(r):g[-(i+1)][c]=8
 return g