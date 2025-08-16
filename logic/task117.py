def p(g):
    # mirror X
    f=sum(g,[])
    for v in f:
        if f.count(v)==5>0<v:
            s={(y,x)for y,r in enumerate(g)for x,c in enumerate(r)if c==v}
            y,x=map(min,zip(*s))
            if{(y,x),(y+2,x),(y,x+2),(y+2,x+2),(y+1,x+1)}<=s:
                s=y+y+2;t=x+x+2
                for y,r in enumerate(g):
                    for x,c in enumerate(r):
                        if c:
                            for Y,X in((y,x),(s-y,x),(y,t-x),(s-y,t-x)):
                                if len(g)>Y>=0<=X<len(g[0]):g[Y][X]=c
                return g
