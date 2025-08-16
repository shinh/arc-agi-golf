def p(g):
    # largest uniform rect
    o=create(16,16);B=0
    for y0 in range(16):
        for x0 in range(16):
            if c:=g[y0][x0]:
                for y1 in range(y0+1,17):
                    for x1 in range(x0+1,17):
                        if all(r[x0:x1]==[c]*(w:=x1-x0)for r in g[y0:y1]) and (a:=(y1-y0)*w)>B:
                            B=a;o=create(16,16)
                            for y in range(y0,y1):o[y][x0:x1]=[c]*w
    return o
