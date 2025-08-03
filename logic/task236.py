def p(g):
    t=g[:4];b=g[5:]
    return [[3*((t[y][x]>0)^(b[y][x]>0))for x in range(4)]for y in range(4)]
