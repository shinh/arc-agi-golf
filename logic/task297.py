# cycle top row colors down the grid
def p(g):
 return (g[:2]+[[c]*len(g[0])for c in g[0]*len(g)])[:len(g)]
