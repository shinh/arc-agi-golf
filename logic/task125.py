def p(g):
    for y in range(15):
        for x in range(15):
            if g[y][x]==6:
                ey,ex=y,x
                while g[ey][x]==6:ey+=1
                while g[y][ex]==6:ex+=1
                for fy in range(y-1,ey+1):
                    for fx in range(x-1,ex+1):
                        if g[fy][fx]==8:
                            g[fy][fx]=3+(y<fy<ey and x<fx<ex)
    return g
