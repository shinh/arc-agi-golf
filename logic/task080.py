def p(g):
    l,b=[(n,c)for c in range(1,10)for n in range(2,9)if{c}=={*g[0][n-1::n]}][0]
    pc,py,px=[(g[y+l][x+l],y+l,x+l)for y in range(0,len(g)-l,l)for x in range(0,len(g[0])-l,l)if(g[y][x]or g[y+l][x])and(g[y][x]or g[y][x+l])and g[y+l][x+l]][0]
    for y in range(0,len(g),l):
        for x in range(0,len(g[0]),l):
            if g[y][x]==pc:
                for ny in range(y-l,y+l*2-1):
                    for nx in range(x-l,x+l*2-1):
                        if 0<=ny<len(g)and 0<=nx<len(g[0]):
                            g[ny][nx]=g[py+ny-y][px+nx-x]
    return g
