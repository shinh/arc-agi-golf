def p(g):
    for t in range(2):
        for y in range(len(g)):
            for x in range(len(g[0])):
                if t:
                    g[y][x]=g[y%10][x%10]
                else:
                    g[y%10][x%10]=g[y][x]
    return g
