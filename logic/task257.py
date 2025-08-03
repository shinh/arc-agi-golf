def p(g):
    return [[next((g[y+Y][x+X]for Y,X in((0,0),(0,5),(5,0),(5,5))if g[y+Y][x+X]),0)for x in range(4)]for y in range(4)]
