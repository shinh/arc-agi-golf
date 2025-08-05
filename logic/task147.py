def p(g):
    for y in range(3):
        for x in range(3):
            if g[y][x]==3:
                q=[(y,x)];g[y][x]=0;c=[(y,x)]
                while q:
                    y1,x1=q.pop()
                    for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
                        ny,nx=y1+dy,x1+dx
                        if 0<=ny<3 and 0<=nx<3 and g[ny][nx]==3:
                            g[ny][nx]=0;q.append((ny,nx));c.append((ny,nx))
                v=8 if len(c)>1 else 3
                for y1,x1 in c:g[y1][x1]=v
    return g
