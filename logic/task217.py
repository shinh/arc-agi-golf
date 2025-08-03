def p(g):
    for y in range(9):
        for x in range(9):
            if g[y][x]:
                b=[r[x//3*3:x//3*3+3] for r in g[y//3*3:y//3*3+3]]
                o=[[0]*9 for _ in range(9)]
                for i in range(3):
                    for j in range(3):
                        if b[i][j]:
                            for a in range(3):
                                for d in range(3):
                                    o[i*3+a][j*3+d]=b[a][d]
                return o
