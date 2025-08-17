def p(g):
    # draw diagonal line when 5 has empty cross arms
    for y,r in enumerate(g):
        for x,c in enumerate(r):
            if c==5:
                for d in 1,-1:
                    a=y-d; b=x+d
                    if r[b]+g[a][x]<1:
                        for i in range(10-abs(a-b)):
                            g[a-min(a,b)+i][b-min(a,b)+i]=f
            elif c:
               f=c
    return[[c-5and c for c in r]for r in g]
