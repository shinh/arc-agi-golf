def p(g):
 # copy pattern blocks
 r=range(len(g))
 return[[g[i][j]or g[5][0]*(g[i%6][j%6]>0)for j in r]for i in r]
