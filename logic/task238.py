def p(g):
    o=g
    # trim until border has {0,8}
    for _ in range(80):o=[*map(list,zip(*o[not{*o[0]}-{0,8}:][::-1]))];g=[*map(list,zip(*g[not{*g[0]}&{8}:][::-1]))]
    L=len(g)
    m=L-1
    for y in range(L):
        for x in range(L):
            if c:=g[y][x]:
                if y>m-x:
                    if y>x:c=o[-1][1]
                    if y<x:c=o[1][-1]
                if y<m-x:
                    if y>x:c=o[1][0]
                    if y<x:c=o[0][1]
            o[y+1][x+1]=c
    return o
