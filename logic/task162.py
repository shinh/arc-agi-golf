def p(g):
    for y in range(len(g)-2):
        for x in range(len(g[0])-2):
            if all(g[y+i][x+j]==0 for i in range(3) for j in range(3)):
                for i in range(3):
                    for j in range(3):
                        g[y+i][x+j]=1
    return g
