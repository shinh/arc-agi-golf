def p(g):
 u=lambda a:[r for i,r in enumerate(a)if r not in a[:i]]
 g=u(g);g=list(map(list,zip(*g)))
 g=u(g);g=list(map(list,zip(*g)))
 g+=g[-2::-1];g=list(map(list,zip(*g)))
 g+=g[-2::-1]
 return g
