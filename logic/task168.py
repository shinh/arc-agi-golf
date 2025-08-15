# 201
def p(g):
    for o in range(4):
        for y in range(9):
            for x in range(9):
                if g[y][x]and g[y+1][x]and g[y][x+1]:
                    for p in range(2,9):
                        if y+p<10 and x+p<10:
                            g[y+p][x+p]=g[y][x]
        g=[*map(list,zip(*g[::-1]))]
    return g
