def p(g):
    # extend from 2s
    r=range(9)
    z=[(y,x)for y in r for x in r if g[y][x]]
    a=[(y,x)for y,x in z if g[y][x]==2]
    c=next(g[y][x]for y,x in z if g[y][x]-2)
    my,mx=map(min,zip(*z))
    for y,x in z:g[y][x]=c
    for y,x in a:
        dy=1-2*(y==my);dx=1-2*(x==mx);t=z
        while(t:=[(Y+dy,X+dx)for Y,X in t if 9>Y+dy>-1<X+dx<9]):
            for Y,X in t:g[Y][X]=c
    return g

