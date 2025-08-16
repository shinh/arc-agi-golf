# first nonzero per nonempty column, zigzag
def p(m):v=[next(filter(None,c))for c in zip(*m)if any(c)]+[0]*9;return[v[:3],v[5:2:-1],v[6:9]]

