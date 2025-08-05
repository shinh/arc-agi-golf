def p(g):
    o=[r[:] for r in g]
    for y in range(10):
        for x in range(10):
            if g[y][x]==8:
                for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
                    ny=y+dy;nx=x+dx
                    while 0<=ny<10 and 0<=nx<10:
                        v=g[ny][nx]
                        if v:
                            if v-8:o[y][x]=v
                            break
                        ny+=dy;nx+=dx
    return o
