# ray casting from 2x2 block
def p(g,o=4):
    for z in range(49):
        if(c:=g[y:=z//7][x:=z%7])*g[y+2][x+2]*(g[y+2][x+1]<1):
            g[y+3][x+3]=c
    return-o*g or p([*map(list,zip(*g[::-1]))],o-1)
