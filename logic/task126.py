def p(g):
    h=len(g);w=len(g[0]);v=set();b=[0]*w
    for y in range(h):
        for x in range(w):
            if g[y][x] and (y,x) not in v:
                c=g[y][x];s=[(y,x)];v.add((y,x));mn=mx=x
                while s:
                    y1,x1=s.pop()
                    mn=min(mn,x1);mx=max(mx,x1)
                    for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
                        ny,nx=y1+dy,x1+dx
                        if 0<=ny<h and 0<=nx<w and g[ny][nx]==c and (ny,nx) not in v:
                            v.add((ny,nx));s.append((ny,nx))
                b[(mn+mx)//2]=4
    g[-1]=b
    return g
