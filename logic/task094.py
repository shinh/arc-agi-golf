def p(g):
    h=[r[:] for r in g]
    v=[[0]*len(g[0]) for _ in g]
    for y in range(len(g)):
        for x in range(len(g[0])):
            if g[y][x]==1 and not v[y][x]:
                q=[(y,x)];v[y][x]=1;Y0=Y1=y;X0=X1=x
                while q:
                    y,x=q.pop();Y0=min(Y0,y);Y1=max(Y1,y);X0=min(X0,x);X1=max(X1,x)
                    for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
                        ny,nx=y+dy,x+dx
                        if 0<=ny<len(g) and 0<=nx<len(g[0]) and g[ny][nx]==1 and not v[ny][nx]:
                            v[ny][nx]=1;q.append((ny,nx))
                cy=(Y0+Y1)//2;cx=(X0+X1)//2
                for i in range(len(g)):
                    if h[i][cx]!=1:h[i][cx]=6
                for j in range(len(g[0])):
                    if h[cy][j]!=1:h[cy][j]=6
    return h
