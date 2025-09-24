def p(g):
    # draw diag when 5 has empty arms
    for y,r in enumerate(g):
        for x,c in enumerate(r):
            if c==5:
                for d in 1,-1:
                    a=y-d;b=x+d
                    if r[b]+g[a][x]<1:
                        for i,v in enumerate(g):
                            j=i+b-a
                            if 0<=j<10:v[j]=f
            elif c:f=c
    return[[c-5and c for c in r]for r in g]
