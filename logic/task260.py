def p(g):
    f=1
    for y in range(9):
        for x in range(9):
            c=g[y][x]
            if c==5:
                sy=-1
                if g[y][x+1]+g[y-1][x]<1:
                    sy=y-1
                    sx=x+1
                if g[y][x-1]+g[y+1][x]<1:
                    sy=y+1
                    sx=x-1
                if sy>=0:
                    m=min(sy,sx)
                    for i in range(10-abs(sy-sx)):
                        g[sy-m+i][sx-m+i]=f
            elif c:
               f=c
    return[[0 if c==5 else c for c in r]for r in g]
