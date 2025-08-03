def p(g):
    o=create(3,3)
    for y,r in enumerate(g):
        for x,v in enumerate(r):
            if v==5:
                for dy in(-1,0,1):
                    for dx in(-1,0,1):
                        c=g[y+dy][x+dx]
                        if c:o[dy+1][dx+1]=c
    return o
