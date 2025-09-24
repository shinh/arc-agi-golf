#201
def p(g):#extend diag from L corners per rot
    r=range(9)
    for o in[0]*4:
        for y in r:
            for x in r:
                for p in((k:=g[y][x])*g[y+1][x]*g[y][x+1]and r[2:10-max(x,y)]or()):g[y+p][x+p]=k
        g[:]=map(list,zip(*g[::-1]))
    return g
