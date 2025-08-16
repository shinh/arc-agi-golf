def p(g):
    # connect matching digits with straight lines
    d={}
    for y,r in enumerate(g):
        for x,v in enumerate(r):
            if v in d:
                Y,X=d.pop(v)
                while X-x or Y-y:g[Y][X]=v;Y+=(Y<y)-(Y>y);X+=(X<x)-(X>x)
            elif v:d[v]=(y,x)
    return g
