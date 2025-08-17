def p(g):
    for o in range(4):
        for y in range(6):
            for x in range(6):
                c=g[y+1][x]
                if g[y][x]<1and c and g[y][x+1]and c in g[y][x+2:]:
                    l=g[y][x+2:].index(c)

                    g=[[[c,5][max([y-ny-l+1,ny-y][ny>y],[x-nx-l+1,nx-x][nx>x])%(l+1)!=1]for nx in range(10)]for ny in range(10)]

        g=[*map(list,zip(*g[::-1]))]
    return g
