def p(g):
 return[[3*(g[y][x]+g[y+5][x]<1)for x in range(4)]for y in range(4)]
