def p(g):
 # max per region
 return[[max(g[y][x]for y in rs for x in cs)for cs in([0],range(1,6),[6])]for rs in([0],[1,2,3],[4])]
