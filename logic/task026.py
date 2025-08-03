def p(g):
    o=create(5,3)
    for y,r in enumerate(g):
        for x in range(3):
            o[y][x]=8*(r[x]+r[x+4]<1)
    return o

