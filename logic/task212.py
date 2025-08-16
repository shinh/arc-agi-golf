# extend lines
def p(g):
 r=g.index([5]*10);[g[k].__setitem__(x,v)for y in range(10)for x,v in enumerate(g[y])if 0<v<3 for k in range(*((0,y+1),(y,10),(y,r),(r+1,y+1))[(v&2)|(y>r)])];return g
