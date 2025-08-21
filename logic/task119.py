# reflect diagonal from 8s off 2s
def p(g):
    for o in range(16):
        for y in range(10):
            for x in range(10):
                if g[y][x]>2<g[y+1][x+1]:
                    c=g[y+2][x+2]
                    if c==g[y+2][x+1]==2>g[y][x+2]:g[y][x+2]=3
                    if c<1:g[y+2][x+2]=3
        g=g[::-1]if o%2 else[*map(list,zip(*g))]
    return g
