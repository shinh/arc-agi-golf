def p(g):
 for r in g:r[0]=r[-1]=8
 g[0]=g[-1]=[8]*len(r)
 return g