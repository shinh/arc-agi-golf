def p(g):
 b=0
 for r in g:
  b=r[-1]=sum(r)or b;s=r.index(b);r[s:]=[b]*len(r[s:])
 return g