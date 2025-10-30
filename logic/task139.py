def p(g):
 b=1>(g[1][0]|g[2][0]|g[3][0])
 # fill red 3x3s
 for y,x in((1,2*b),(4+2*b,5)):
  for r in g[y:y+3]:
   r[x:x+3]=[c or 7 for c in r[x:x+3]]
 return g
