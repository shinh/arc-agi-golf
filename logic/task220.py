def p(g):
    h=len(g);w=len(g[0]);o=create(h,w);d={2:1,3:6,8:4}
    for y,r in enumerate(g):
        for x,c in enumerate(r):
            if c in d:
                for Y in range(max(0,y-1),min(h,y+2)):
                    for X in range(max(0,x-1),min(w,x+2)):o[Y][X]=d[c]
                o[y][x]=c
    return o
