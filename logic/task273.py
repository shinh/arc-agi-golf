def p(g):
    rows=[{x for x,v in enumerate(r) if v==4} for r in g]
    for y1 in range(10):
        c1=rows[y1]
        if c1:
            for y2 in range(y1+1,10):
                com=sorted(c1&rows[y2])
                for i in range(len(com)):
                    for j in range(i+1,len(com)):
                        a,b=com[i],com[j]
                        for y in range(y1+1,y2):
                            for x in range(a+1,b):g[y][x]=2
    return g
