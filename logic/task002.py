def p(g):
 for t in range(80):
  g=[*zip(*[[[c,1][c+n==1]for c,n in zip(r,[*r[1:],1])]for r in g][::-1])]
 return[[b'\0'[c]for c in r]for r in g]
