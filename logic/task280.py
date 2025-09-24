def p(g):
    # expand bars from each 2
    for o in range(4):
        for y,r in enumerate(g):
            n=w=0
            for x,c in enumerate(r):
                if c==3:n+=1;w=0
                if c==0:
                    if w:
                        for d in range(-n,n+1):
                            if 0<=y+d<len(g):
                                g[y+d][x]=2+(d!=0)
                    n*=w
                w|=c==2
        g=[*map(list,zip(*g[::-1]))]
    return g
