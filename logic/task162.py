def p(g):
    for y in range(18):
        for x in range(18):
            if all(g[y+i][x+j]==0 for i in range(3)for j in range(3)):
                for i in range(3):
                    for j in range(3):
                        g[y+i][x+j]=1
    return g
