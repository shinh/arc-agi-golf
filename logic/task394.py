def p(g):
    h=len(g);w=len(g[0])
    for py in range(1,h+1):
        if all(g[y][x]==g[y+py][x] or 0 in (g[y][x],g[y+py][x]) for y in range(h-py) for x in range(w)):break
    for px in range(1,w+1):
        if all(g[y][x]==g[y][x+px] or 0 in (g[y][x],g[y][x+px]) for x in range(w-px) for y in range(h)):break
    ys=[i for i,r in enumerate(g) if 0 in r];xs=[j for j in range(w) if any(g[i][j]==0 for i in range(h))]
    y0,y1=min(ys),max(ys);x0,x1=min(xs),max(xs)
    t=off=None
    for a in range(h-py+1):
        for b in range(w-px+1):
            sub=[r[b:b+px] for r in g[a:a+py]]
            if all(all(c for c in row) for row in sub): t=sub;off=(a,b);break
        if t: break
    if not t:
        t=[[0]*px for _ in range(py)];off=(0,0)
        for y in range(h):
            for x in range(w):
                if g[y][x]: t[y%py][x%px]=g[y][x]
    a,b=off
    return [[t[(y-a)%py][(x-b)%px] for x in range(x0,x1+1)] for y in range(y0,y1+1)]
