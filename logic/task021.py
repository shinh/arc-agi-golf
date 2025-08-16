def p(g):
    a=g[0][0];f=lambda t:-~sum(a not in r for r in t);return[[a]*f(zip(*g))]*f(g) # fill top-left block
