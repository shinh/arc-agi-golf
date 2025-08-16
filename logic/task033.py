def p(g):
 # copy pattern blocks
 c=g[5][0];r=range(len(g))
 [g[i].__setitem__(j,c)for i in r for j in r if g[i%6][j%6]and g[i][j]<1]
 return g
