def p(g):
    h=len(g);w=len(g[0])
    for y in range(h-1):
        for x in range(w-1):
            if not sum(g[y+i][x+j] for i in(0,1) for j in(0,1)):
                for i in(0,1):
                    for j in(0,1):
                        g[y+i][x+j]=2
    return g
