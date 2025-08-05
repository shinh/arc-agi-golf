def p(g):
    h=len(g)//2;w=len(g[0])
    return[[2*(g[y][x]==g[y+h][x]==0)for x in range(w)]for y in range(h)]
