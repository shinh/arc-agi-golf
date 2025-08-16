def p(g):
    # find shift and repeat
    w=len(g[0])
    fg=[(i,j,v)for i,r in enumerate(g)for j,v in enumerate(r)if v]
    dy,dx=max((m,dy,dx)for dy in range(1,6)for dx in range(-w,w)if(m:=sum((i+dy,j+dx,v)in fg for i,j,v in fg)))[1:]
    out=[[0]*w for _ in range(10)]
    for i,j,v in fg:
        y=i;x=j
        while 0<=y<10 and 0<=x<w:out[y][x]=v;y+=dy;x+=dx
    return out
