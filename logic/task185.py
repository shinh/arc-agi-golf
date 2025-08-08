def p(g):
    sx=sy=99
    for y in range(len(g)):
        for x in range(len(g[0])):
            if g[y][x]not in g[0]:
                sx=min(sx,x)
                sy=min(sy,y)
                l=(y-sy)//3
    return[[g[sy+l*y][sx+l*x]*(g[sy+l*y][sx+l*x]not in g[0]and g[sy+l*y][sx+l*x]==g[sy+l*y+l][sx+l*x]==g[sy+l*y][sx+l*x+l]==g[sy+l*y+l][sx+l*x+l])for x in(0,1,2)]for y in(0,1,2)]
