def p(g):
    h=len(g);w=len(g[0])
    for y in range(h):
        for x in range(w):
            if g[y][x]==2 and all(not(0<=y+dy<h and 0<=x+dx<w and g[y+dy][x+dx]==2) for dy,dx in ((1,0),(-1,0),(0,1),(0,-1))):
                g[y][x]=1
    return g
