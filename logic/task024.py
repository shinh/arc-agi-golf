# propagate 1/3 rows and 2 columns
def p(g):
 Z=[2in c for c in zip(*g)]
 return[[1if 1in R else 3if 3in R else 2if v<1and Z[c]else v for c,v in enumerate(R)]for R in g]

