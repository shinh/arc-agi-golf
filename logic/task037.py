def p(g):
    # connect matching digits with straight lines
    d={}
    for y,r in enumerate(g):
        for x,v in enumerate(r):
            if v in d:
                Y,X=d.pop(v)
                dy=(Y>y)-(Y<y);dx=(X>x)-(X<x)
                for i in range(abs(Y-y)+1):g[y+i*dy][x+i*dx]=v
            elif v:d[v]=(y,x)
    return g
