def p(g):
    h=len(g);w=len(g[0]);o=[r[:] for r in g]
    for y in range(h):
        for x in range(w):
            if g[y][x]==8:
                for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
                    ny=y+dy;nx=x+dx
                    while 0<=ny<h and 0<=nx<w:
                        v=g[ny][nx]
                        if v:
                            if v-8:o[y][x]=v
                            break
                        ny+=dy;nx+=dx
    return o
