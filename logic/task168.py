# 201
def p(g):# extend diagonal from L-corner in all rotations
    r=range(9)
    for o in[0]*4:
        for y in r:
            for x in r:
                if(k:=g[y][x])*g[y+1][x]*g[y][x+1]:
                    for p in r[2:10-max(x,y)]:g[y+p][x+p]=k
        g[:]=map(list,zip(*g[::-1]))
    return g
