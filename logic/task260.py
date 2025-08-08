def p(g):
    for y in range(9):
        for x in range(9):
            c=g[y][x]
            if c==5:
                for sy,sx in(y-1,x+1),(y+1,x-1):
                    if g[y][sx]+g[sy][x]<1:
                        for i in range(10-abs(sy-sx)):
                            g[sy-min(sy,sx)+i][sx-min(sy,sx)+i]=f
            elif c:
               f=c
    return[[0 if c==5 else c for c in r]for r in g]
