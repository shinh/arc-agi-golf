def p(g):
    m=1
    while m:
        m=0
        for y,r in enumerate(g):
            for x,v in enumerate(r):
                if v==1 and (y and g[y-1][x]>2)+(y<16 and g[y+1][x]>2)+(x and r[x-1]>2)+(x<16 and r[x+1]>2)>1:
                    r[x]=3;m=1
    return g
