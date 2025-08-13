def p(g):
    v=[[0]*(len(g)+1)]+[[0]+r for r in g]
    for c in range(10):
        for y in range(8):
            for x in range(8):
                if(y or x)and all((v[i//4][i%4]>0)==(v[y+i//4][x+i%4]==c)for i in range(16))and c!=5:
                    for i in range(9):
                        if g[y+i//3][x+i%3]:
                            g[y+i//3][x+i%3]=5
    return g
