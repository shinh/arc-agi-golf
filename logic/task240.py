def p(g,E=enumerate):
    # mirror colors and spread them through rotated scans
    for y,r in E(g):
        for x,c in E(r):
            if c:r[x]=g[18-y][x]=r[18-x]=g[18-y][18-x]=c
    for y,r in E(g):
        for x,c in E(r):
            if c and y+1<x<17-y and x%2:
                for j in range(x,17-y,2):r[j]=c
    g=[*map(list,zip(*g[::-1]))]
    for y,r in E(g):
        for x,c in E(r):
            if c and y+1<x<17-y and x%2:
                for j in range(x,17-y,2):r[j]=c
    g=[*map(list,zip(*g[::-1]))]
    for y,r in E(g):
        for x,c in E(r):
            if c and y+1<x<17-y and x%2:
                for j in range(x,17-y,2):r[j]=c
    g=[*map(list,zip(*g[::-1]))]
    for y,r in E(g):
        for x,c in E(r):
            if c and y+1<x<17-y and x%2:
                for j in range(x,17-y,2):r[j]=c
    g=[*map(list,zip(*g[::-1]))]
    return g
