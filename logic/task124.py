def p(g):
    # find shift and repeat
    # pick dy,dx maximizing overlap then tile non-zero cells along that vector
    fg=[(i,j,v)for i,r in enumerate(g)for j,v in enumerate(r)if v]
    dy,dx=max((sum((y+dy,x+dx,v)in fg for y,x,v in fg),dy,dx)for dy in range(1,6)for dx in range(-10,10))[1:]
    out=[[0]*10 for _ in[0]*10]
    for y,x,v in fg:
        while 10>y>=0<=x<10:out[y][x]=v;y+=dy;x+=dx
    return out
