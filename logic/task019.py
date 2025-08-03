def p(g):
    h=len(g);w=len(g[0])
    o=[[8*((y+x)%2==0) for x in range(w*2)] for y in range(h*2)]
    for y in range(h*2):
        for x in range(w*2):
            v=g[y%h][x%w]
            if v:o[y][x]=v
    return o
