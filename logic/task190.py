# ray casting from 2x2 block
def p(g,o=3):
    for z in range(49):y=z//7;x=z%7;a=g[y+2];g[y+3][x+3]|=g[y][x]*(a[x+2]>a[x+1])
    return-o*g or p([*map(list,zip(*g[::-1]))],o-1)
