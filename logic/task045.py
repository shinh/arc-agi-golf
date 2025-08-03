def p(g):
 for r in g:
  if r[0]==r[-1]>0:r[:]=[r[0]]*len(r)
 return g
