# rotate the grid so flood fill can flow from one side only
def p(g):
 g[0][0]=1;g[9][9]=3
 for r in g[4:6]:r[4:6]=r[4]or 2,r[5]or 2
 for _ in' '*12:g=[[a or b%5 for a,b in zip(r,(5,)+r)]for r in zip(*g[::-1])]
 return g

