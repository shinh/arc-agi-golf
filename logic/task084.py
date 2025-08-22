def p(g):
# fill bottom row with 4s and draw diagonal of 2s
 i=1
 while i<len(g):g[-1][i]=4;g[~i][i]=2;i+=1
 return g

