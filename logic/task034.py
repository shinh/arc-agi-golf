def p(g):
    # extend from 2s
    o=[r[:]for r in g]
    z=[(y,x)for y,r in enumerate(g)for x,v in enumerate(r)if v]
    c=[g[y][x]for y,x in z if g[y][x]-2][0]
    my=min(y for y,_ in z);mx=min(x for _,x in z)
    for y,x in z:o[y][x]=c
    for y,x in z:
        if g[y][x]==2:
            dy=1-2*(y==my);dx=1-2*(x==mx)
            t=z
            while t:
                t=[(Y+dy,X+dx)for Y,X in t if 9>Y+dy>-1<X+dx<9]
                for Y,X in t:o[Y][X]=c
    return o

