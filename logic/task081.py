def p(g):
    h=w=7;o=[r for r in g]
    for y in range(h):
        for x in range(w):
            if g[y][x]==8:
                for dy in(-1,1):
                    ny=y+dy
                    if 0<=ny<h and g[ny][x]==8:
                        if x and g[y][x-1]==0 and g[ny][x-1]==8:o[y][x-1]=1
                        if x<6 and g[y][x+1]==0 and g[ny][x+1]==8:o[y][x+1]=1
    return o
