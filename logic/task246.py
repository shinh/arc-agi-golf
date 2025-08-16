def p(g):
    # connect 2 to 3 with 8s
    f=sum(g,[])
    y,x=divmod(f.index(2),w:=len(g[0]));Y,X=divmod(f.index(3),w)
    while x!=X:g[y][x:=x+(X>x)-(X<x)]=8
    while y!=Y:g[y:=y+(Y>y)-(Y<y)][x]=8
    g[Y][X]=3;return g
