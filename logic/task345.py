def p(g):
    w=h=10;o=[g[-1][:]for _ in g]
    for y in range(h-1,-1,-1):
        for x,v in enumerate(g[y]):
            if v==5:
                if o[y][x]==2:
                    o[y][x]=5
                    if x+1<w:
                        o[y][x+1]=2
                        if y+1<h:o[y+1][x+1]=2
                        for r in range(y):
                            if o[r][x]==2:o[r][x]=0;o[r][x+1]=2
                else:o[y][x]=5
    return o
