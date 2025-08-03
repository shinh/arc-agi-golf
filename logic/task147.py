def p(g):
    h=len(g);w=len(g[0])
    for y in range(h):
        for x in range(w):
            if g[y][x]==3:
                q=[(y,x)];g[y][x]=0;c=[(y,x)]
                while q:
                    y1,x1=q.pop()
                    for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx=y1+dy,x1+dx
                        if 0<=ny<h and 0<=nx<w and g[ny][nx]==3:
                            g[ny][nx]=0;q.append((ny,nx));c.append((ny,nx))
                v=8 if len(c)>1 else 3
                for y1,x1 in c:g[y1][x1]=v
    return g
