def p(g):
    # largest uniform rect
    B=0
    for y0 in range(16):
        for x0 in range(16):
            c=g[y0][x0]
            if c:
                for y1 in range(y0+1,17):
                    for x1 in range(x0+1,17):
                        if all(g[y][x]==c for y in range(y0,y1) for x in range(x0,x1)) and (a:=(y1-y0)*(x1-x0))>B:
                            B,R=a,(y0,y1,x0,x1,c)
    o=create(16,16)
    if B:
        y0,y1,x0,x1,c=R
        for y in range(y0,y1):o[y][x0:x1]=[c]*(x1-x0)
    return o
