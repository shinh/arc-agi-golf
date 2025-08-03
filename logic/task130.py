def p(g):
    return [[max(b:=[g[y+i][x+j]for i in range(3)for j in range(3)],key=b.count)for x in(0,3,6)]for y in(0,3,6)]
