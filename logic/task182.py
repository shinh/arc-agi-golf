def p(g):
    # find the top-left of frame and recolor matching shapes
    for y in range(16):
        for x in range(16):
            if g[y][x]==g[y+1][x]==g[y][x+1]==5:
                sx=x
                sy=y
    for y in range(16):
        for x in range(16):
            if all((g[sy+dy+1][sx+dx+1]>0)==(g[y+dy][x+dx]>0)for dy in range(5)for dx in range(5)):
                for dy in range(5):
                    for dx in range(5):
                        g[y+dy][x+dx]=g[sy+dy+1][sx+dx+1]
    return g
