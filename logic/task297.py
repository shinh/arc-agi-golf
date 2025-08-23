# fill rows >=2 with cycling colors from the top row
def p(g):
 for r,c in zip(g[2:],g[0]*len(g)):r[:]=[c]*len(r)
 return g
