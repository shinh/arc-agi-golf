def p(g):
    c=min({v for r in g for v in r if v>1})
    h=len(g);w=len(g[0]);ps=[]
    for y in range(1,h-1):
        for x in range(1,w-1):
            if g[y][x]==g[y-1][x]==g[y+1][x]==g[y][x-1]==g[y][x+1]==1 and all(g[y+a][x+b]!=1 for a in(-1,1) for b in(-1,1)):ps+=[(y,x)]
    for y,x in ps:g[y][x]=g[y-1][x]=g[y+1][x]=g[y][x-1]=g[y][x+1]=c
    return g
