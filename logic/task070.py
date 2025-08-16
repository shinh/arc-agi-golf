def p(g):
    # grow 3s over 1s with >=2 big neighbors
    for y,r in enumerate(g):
        for x in range(17):
            if r[x]==1<sum((y and 2<g[y-1][x],y<16 and 2<g[y+1][x],x and 2<r[x-1],x<16 and 2<r[x+1])):
                r[x]=3
                return p(g)
    return g
