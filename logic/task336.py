def p(g):
    for o in range(4):
        for y in range(10):
            for x in range(10):
                if g[y][x]==5:
                    ey,ex=y,x
                    while ey<10and g[ey][x]==5:ey+=1
                    while ex<10and g[y][ex]==5:ex+=1
                    ey-=1
                    for fy in range(y+1,ey):
                        for fx in range(x+1,ex-1):
                            g[fy][fx]=8
                    if g[ey][x:ex].count(0)==1:
                        #print('zzz',g[ey][x:ex])
                        x=g[ey].index(0,x)
                        for fy in range(ey,10):
                            g[fy][x]=8

        g=[*map(list,zip(*g[::-1]))]
    return g