def p(g):
 return [[next((g[y][x] for y in rs for x in cs if g[y][x]),0)for cs in([0],range(1,6),[6])]for rs in([0],range(1,4),[4])]
