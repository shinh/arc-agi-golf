def p(g):
    sx=sy=99
    ex=ey=-1
    for y in range(len(g)):
        for x in range(len(g[0])):
            if g[y][x]==4:
                sx=min(sx,x)
                sy=min(sy,y)
                ex=max(ex,x)
                ey=max(ey,y)
    o=[[g[sy+y][sx+x]for x in range(ex-sx+1)]for y in range(ey-sy+1)]

    sx2=sy2=99
    ex2=ey2=-1
    for y in range(len(g)):
        for x in range(len(g[0])):
            if g[y][x]and(x<sx or y<sy or ex<x or ey<y):
                sx2=min(sx2,x)
                sy2=min(sy2,y)
                ex2=max(ex2,x)
                ey2=max(ey2,y)

    no_mirror=any(g[y+sy2][sx2]==o[y+1][0]for y in range(ey2-sy2+1))
    for y in range(sy2,ey2+1):
        for x in range(sx2,ex2+1):
            o[y-sy2+1][[sx2-x-2,x-sx2+1][no_mirror]]=g[y][x]
    return o
