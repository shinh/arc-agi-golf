def p(g):# grow block
 r=g[0]
 for _ in r[2::2]:r=r[:];r[r.index(0)]=r[0];g+=r,
 return g
