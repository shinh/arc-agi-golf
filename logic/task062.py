def p(g):
    # mirror shape across line of 2s
    o=[[3]*10 for _ in g]
    Y=X=()
    for y,r in enumerate(g):
        for x,v in enumerate(r):
            if v==2:t=x;z=y
            elif v:Y+=y,;X+=x,;c=v
    v=z in Y
    a=(t+(max,min)[t<min(X)](X),z+(max,min)[z<min(Y)](Y))[v^1]
    for y,x in zip(Y,X):o[y][x]=o[[y,a-y][v^1]][[x,a-x][v]]=c
    return o
