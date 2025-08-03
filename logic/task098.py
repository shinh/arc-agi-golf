def p(g):
    h=[r[:] for r in g];v=[[0]*len(g[0]) for _ in g]
    for y in range(len(g)):
        for x in range(len(g[0])):
            c=g[y][x]
            if c and not v[y][x]:
                q=[(y,x)];v[y][x]=1;Y0=Y1=y;X0=X1=x
                while q:
                    y,x=q.pop();Y0=min(Y0,y);Y1=max(Y1,y);X0=min(X0,x);X1=max(X1,x)
                    for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
                        ny=y+dy;nx=x+dx
                        if 0<=ny<len(g) and 0<=nx<len(g[0]) and g[ny][nx]==c and not v[ny][nx]:
                            v[ny][nx]=1;q.append((ny,nx))
                for yy in range(Y0,Y1+1):
                    for xx in range(X0,X1+1):
                        h[yy][xx]=c if yy in(Y0,Y1) or xx in(X0,X1) else 0
    return h
