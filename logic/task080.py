def p(g):
    # spread learned pattern
    R=range
    l=[n for c in R(1,10)for n in R(2,9)if{c}=={*g[0][n-1::n]}][0]
    pc,py,px=[(g[y+l][x+l],y+l,x+l)for y in R(0,len(g)-l,l)for x in R(0,len(g[0])-l,l)if(g[y][x]or g[y+l][x]and g[y][x+l])and g[y+l][x+l]][0]
    for y in R(0,len(g),l):
        for x in R(0,len(g[0]),l):
            if g[y][x]==pc:
                for ny in R(y-l,y+l*2-1):
                    for nx in R(x-l,x+l*2-1):
                        if 0<=ny<len(g)and 0<=nx<len(g[0]):
                            g[ny][nx]=g[py+ny-y][px+nx-x]
    return g

