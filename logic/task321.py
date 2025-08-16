def p(g):
 # prefer left then mid else keep
 return[[r[c]or r[c+5]or r[c-4]for c in range(4)]for r in g]

