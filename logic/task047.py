def p(g):
    for y in range(9):
        for x in range(9):
            if g[y][x]==8:A=y,x
            elif g[y][x]==7:B=y,x
    o=create(9,9);y,x=A;Y,X=B
    for i in range(9):
        o[y][i]=o[i][x]=8
        o[Y][i]=o[i][X]=7
    o[y][X]=o[Y][x]=2
    return o
