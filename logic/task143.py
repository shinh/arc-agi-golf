# 213
def p(g):
    v=[[0]+r for r in[[0]*99]+g]
    for c in range(10):
        for y in range(8):
            for x in range(8):
                if(y>4or x>4)and all((v[i//4][i%4]>0)==(v[y+i//4][x+i%4]==c)for i in range(16)):
                    for i in range(9):
                        g[y+i//3][x+i%3]=g[y+i//3][x+i%3]and 5
    return g
