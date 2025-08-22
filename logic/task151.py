def p(g):# draw ring around the all-1 row/col
 f=lambda a:[*map(all,a)].index(1);x,y=f(g),f(zip(*g))
 for i in-1,1:g[x+i][y-1:y+2]=4,4,4;g[x][y+i]=4
 return g
