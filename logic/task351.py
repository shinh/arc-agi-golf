def p(g,R=range(16),o=[]):
    for y in R:
        r=[g[15-y][15-x]for x in R if g[y][x]==3]
        if r:o+=r,
    return o
