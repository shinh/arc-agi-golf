def p(g):
    # mirror non9
    e=enumerate
    for k in range(4):
        for i,j,v in[(i,j,v)for i,r in e(g)for j,v in e(r)if v-9]:
            x=(j,i^31,i^31,i)[k]
            y=(i,j^31,j,j^31)[k]
            if x<30>y:g[x][y]=v
    return g
