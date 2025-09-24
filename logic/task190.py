# ray casting from 2x2 block
def p(g,o=3):
    for z in range(49):g[(y:=z//7)+3][(x:=z%7)+3]|=g[y][x]*(g[y+2][x+1]<1<=g[y+2][x+2])
    return-o*g or p([*map(list,zip(*g[::-1]))],o-1)
