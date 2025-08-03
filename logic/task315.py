def p(g):
    o=create(9,9)
    for y in range(3):
        for x in range(3):
            if g[y][x]==2:
                for Y in range(3):
                    for X in range(3):
                        o[y*3+Y][x*3+X]=g[Y][X]
    return o
