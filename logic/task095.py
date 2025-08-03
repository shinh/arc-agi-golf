def p(g):
    h=[r[:] for r in g]
    for y,r in enumerate(g):
        for x,c in enumerate(r):
            if c==5:
                for dy in(-1,0,1):
                    for dx in(-1,0,1):
                        ny=y+dy;nx=x+dx
                        if 0<=ny<len(g) and 0<=nx<len(g[0]):h[ny][nx]=1
                h[y][x]=5
    return h
