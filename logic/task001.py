def p(g):
    o=create(9,9)
    for y in range(9):
        for x in range(9):
            c=g[y//3][x//3]
            if c:
                o[y][x]=g[y%3][x%3]
    return o