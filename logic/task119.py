# reflect diagonal from 8s off 2s
def p(g):
    for o in range(16):
        for y in range(10):
            for x in range(10):
                if g[y][x]in(3,8)and g[y+1][x+1]in(3,8):
                    c=g[y+2][x+2]
                    if c==2 and g[y+2][x+1]==2 and g[y][x+2]==0:
                        g[y][x+2]=3
                    if c==0:
                        g[y+2][x+2]=3
        if o%2:g=zip(*g[::-1])
        g=[*map(list,zip(*g))]
    return g
