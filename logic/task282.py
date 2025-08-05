def p(g):
    h=len(g);w=len(g[0])
    o=create(h,w)
    for y in range(h):
        for x in range(w):
            if g[y][x]==5:
                for dy,dx,c in ((-1,0,1),(1,0,1),(0,-1,1),(0,1,1),(-1,-1,5),(-1,1,5),(1,-1,5),(1,1,5)):
                    ny=y+dy;nx=x+dx
                    if 0<=ny<h and 0<=nx<w:o[ny][nx]=c
    return o
