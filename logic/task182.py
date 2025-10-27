def p(g):
    # find the top-left of frame and recolor matching shapes
    for y in range(16):
        for x in range(16):
            if g[y][x]==5==g[y][x+1]==g[y+1][x]:sx,sy=x,y
    for y in range(16):
        for x in range(16):
            if[g[sy+dy+1][sx+dx+1]>0for dy in range(5)for dx in range(5)]==[g[y+dy][x+dx]>0for dy in range(5)for dx in range(5)]:
                for dy in range(5):
                    for dx in range(5):
                        g[y+dy][x+dx]=g[sy+dy+1][sx+dx+1]
    return g
