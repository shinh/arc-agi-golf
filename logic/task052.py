def p(g):
    return[[5]*3 if len({*r})<2 else[0]*3 for r in g]
