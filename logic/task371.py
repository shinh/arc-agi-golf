def p(g):
    a=[(y,x) for y,r in enumerate(g) for x,v in enumerate(r) if v==1]
    (y1,x1),(y2,x2)=a
    y=(y1+y2)//2;x=(x1+x2)//2
    g[y][x-1]=g[y][x]=g[y][x+1]=g[y-1][x]=g[y+1][x]=3
    return g
