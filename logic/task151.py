def p(g):# draw ring around the all-1 row/col
 x,y=[[*map(all,h)].index(1)for h in(g,zip(*g))]
 for i in-1,1:g[x+i][y-1:y+2]=4,4,4;g[x][y+i]=4
 return g
