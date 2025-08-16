def p(g):
    # mirror shape across line of 2s
    o=[[3]*10 for _ in g]
    Y=[];X=[];t=[]
    for y,r in enumerate(g):
        for x,v in enumerate(r):
            if v==2:t+=x,;z=y
            elif v:Y+=y,;X+=x,;c=v
    v=min(Y)<=z<=max(Y)
    a=(t[0]+(max,min)[t[0]<min(X)](X),z+(max,min)[z<min(Y)](Y))[not v]
    for y,x in zip(Y,X):o[y][x]=o[[y,a-y][not v]][[x,a-x][v]]=c
    return o
