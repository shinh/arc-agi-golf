def p(g):
    # locate anchor shape and pour colors downward from it
    for y in range(3,20):
        for x in range(6,20):
            c=g[y][x]
            if c and all(g[y+u][x+v]==c for u,v in [(0,0),(0,-6),(-1,-1),(-1,-2),(-1,-4),(-1,-5),(-2,-2),(-2,-3),(-2,-4),(-3,-3)]):
                for i,d in enumerate([1,0,0,-1,0,0,1]):
                    X=x-i;Y=y+d
                    for k in range(Y,20):
                        t=g[k][X]
                        if t:
                            for k in range(Y,20):g[k][X]=t
                            break
                return g
