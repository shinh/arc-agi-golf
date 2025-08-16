def p(g):#move 5s toward 2 cluster
    Y,X=zip(*[(y,x)for y,r in enumerate(g)for x,v in enumerate(r)if v==2])
    y0=min(Y)-1;y1=max(Y)+1;x0=min(X)-1;x1=max(X)+1
    o=[[v==2 and 2 for v in r]for r in g]
    for y,x in[(y,x)for y,r in enumerate(g)for x,v in enumerate(r)if v==5]:
        o[min(y1,max(y0,y))][min(x1,max(x0,x))]=5
    return o
