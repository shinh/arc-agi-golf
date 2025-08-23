def p(g):
    # connect2-3 w8s
    f=sum(g,[]);w=len(g[0]);(y,x),(Y,X)=[divmod(f.index(i),w)for i in(2,3)]
    while y-Y or x-X:x+=(X>x)-(X<x);g[y][x]=8;y+=(x==X)*((Y>y)-(Y<y))
    return g
