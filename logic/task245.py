def p(g):
    R=[(y,x)for y,r in enumerate(g)for x,v in enumerate(r)if v==3]
    P=[(y,x)for y,r in enumerate(g)for x,v in enumerate(r)if v==2]
    t=min(y for y,_ in R);l=min(x for _,x in R)
    dy=t+1-min(y for y,_ in P);dx=l+1-min(x for _,x in P)
    o=[[0]*len(g[0])for _ in g]
    for y,x in P:o[y+dy][x+dx]=2
    for y,x in R:o[y][x]=3
    return o
