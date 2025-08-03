def p(g):
    o=[r[:] for r in g]
    for y in range(len(g)-2):
        for x in range(len(g[0])-2):
            if [g[y+i][x:x+3] for i in range(3)]==[[1,1,1],[1,0,1],[1,1,1]]:
                o[y][x]=o[y][x+2]=o[y+2][x]=o[y+2][x+2]=0
                o[y][x+1]=o[y+1][x]=o[y+1][x+1]=o[y+1][x+2]=o[y+2][x+1]=2
    return o
