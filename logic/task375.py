# zero both diagonals
def p(g):
 i=-1
 for r in g:r[i:=i+1]=r[~i]=0
 return g