def p(g):
 n=len(g)
 for t in range(100):
  g[0]=[[c,1][c==0]for c in g[0]]
  g=[[[r[x],1][r[x]==0and(r*2)[x+1]==1]for x in range(len(r))]for r in g]
  g=[*zip(*g[::-1])]
 return[[[4,0,0,3][c]for c in r]for r in g]
