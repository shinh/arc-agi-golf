def p(g):
    for y,r in enumerate(g):
        for x,v in enumerate(r):
            if v==2:a=(y,x)
            if v==3:b=(y,x)
    y,x=a;Y,X=b
    s=1 if X>x else -1
    while x!=X:
        x+=s
        if (y,x)!=b:g[y][x]=8
    s=1 if Y>y else -1
    while y!=Y:
        y+=s
        if (y,x)!=b:g[y][x]=8
    return g
