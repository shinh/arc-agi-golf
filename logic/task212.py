# extend lines
def p(g):
 r=[v.count(5)>9 for v in g].index(1);[g[k].__setitem__(x,v)for y,R in enumerate(g)for x,v in enumerate(R)if 0<v<3 for k in range(*((0,y+1),(y,10),(y,r),(r+1,y+1))[(v&2)|(y>r)])];return g
