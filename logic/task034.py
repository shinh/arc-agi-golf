def p(g):
    # extend from 2s
    z=[(y,x,g[y][x])for y in range(9) for x in range(9) if g[y][x]]
    c=next(v for y,x,v in z if v-2)
    my,mx,_=map(min,zip(*z))
    for y,x,v in z:
        if v==2:
            dy=1-2*(y==my);dx=1-2*(x==mx)
            for Y,X,_ in z:
                while-1<(Y:=Y+dy)<9>-1<(X:=X+dx)<9:
                    g[Y][X]=c
        g[y][x]=c
    return g

