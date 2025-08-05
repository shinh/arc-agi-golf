def p(g):
    h=len(g);w=len(g[0])
    o=[[g[y%h][x%w] for x in range(w*2)]for y in range(h*2)]
    c=[(y,x)for y in range(h*2)for x in range(w*2)if o[y][x]]
    for y,x in c:
        for dy,dx in(-1,-1),(-1,1),(1,-1),(1,1):
            Y=y+dy;X=x+dx
            if 0<=Y<h*2 and 0<=X<w*2 and o[Y][X]==0:o[Y][X]=8
    return o
