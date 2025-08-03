def p(g):
    for y,r in enumerate(g):
        for x,v in enumerate(r):
            if v!=2 and any(0<=y+dy<len(g) and 0<=x+dx<len(r) and g[y+dy][x+dx]==2 for dy in(-1,0,1) for dx in(-1,0,1) if dx or dy):
                if v in {1,3,8}:g[y][x]=4
    return g
