def p(g):
    o=g
    for i in range(80):
        o=[*map(list,zip(*o[not{*o[0]}-{0,8}:][::-1]))]
        g=[*map(list,zip(*g[not{*g[0]}&{8}:][::-1]))]

    L=len(g)
    for y in range(L):
        for x in range(L):
            c=g[y][x]
            if c:
                if y>x and y>L-x-1:c=o[-1][1]
                if y>x and y<L-x-1:c=o[1][0]
                if y<x and y<L-x-1:c=o[0][1]
                if y<x and y>L-x-1:c=o[1][-1]
            o[y+1][x+1]=c
    return o
