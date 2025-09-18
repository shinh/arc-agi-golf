def p(g):
    a=g[0][0];return[[a]*-~sum(c!=a for c in g[0])]*-~sum(r[0]!=a for r in g) # fill top-left block
