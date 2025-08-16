def p(g):
    # shift 2s below-right of the top-left 3
    R=[(y,x)for y,r in enumerate(g)for x,v in enumerate(r)if v==3]
    P=[(y,x)for y,r in enumerate(g)for x,v in enumerate(r)if v==2]
    a,b=map(min,zip(*R));c,d=map(min,zip(*P))
    o=[[0]*len(r)for r in g]
    for y,x in P:o[y+a-c+1][x+b-d+1]=2
    for y,x in R:o[y][x]=3
    return o
