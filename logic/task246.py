def p(g):
    for y,r in enumerate(g):
        for x,v in enumerate(r):
            if v==2:a=(y,x)
            if v==3:b=(y,x)
    y,x=a;Y,X=b
    s=[-1,1][X>x]
    while x!=X:
        x+=s
        if (y,x)!=b:g[y][x]=8
    s=[-1,1][Y>y]
    while y!=Y:
        y+=s
        if (y,x)!=b:g[y][x]=8
    return g
