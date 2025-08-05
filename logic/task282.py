def p(g):
    o=create(9,9)
    for y in range(9):
        for x in range(9):
            if g[y][x]==5:
                for dy,dx,c in ((-1,0,1),(1,0,1),(0,-1,1),(0,1,1),(-1,-1,5),(-1,1,5),(1,-1,5),(1,1,5)):
                    ny=y+dy;nx=x+dx
                    if 0<=ny<9 and 0<=nx<9:o[ny][nx]=c
    return o
