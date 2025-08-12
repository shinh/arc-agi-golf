def p(g):
    H=len(g)
    y_borders=[]
    for y in range(H):
        if max(g[y],key=g[y].count):
            y_borders.append(y)
    x_borders=[]
    for x in range(len(g[0])):
        r=[g[y][x] for y in range(H)]
        if max(r,key=r.count):
            x_borders.append(x)

    o=[[g[y][x]for x in range(x_borders[0],x_borders[-1]+1)]for y in range(y_borders[0],y_borders[-1]+1)]

    for _ in range(4):
        for r in o:
            for x in range(r.index(r[-1]),len(r)):
                r[x]=r[-1]
        o=[*map(list,zip(*o[::-1]))]

    return o
