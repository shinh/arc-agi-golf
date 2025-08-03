def p(g):
    h=len(g);w=len(g[0]);v=set();d=((1,0),(-1,0),(0,1),(0,-1))
    for y in range(h):
        for x in range(w):
            if g[y][x]==1 and (y,x)not in v:
                s=[(y,x)];v.add((y,x));Y=[y];X=[x];C=[]
                while s:
                    y1,x1=s.pop();C.append((y1,x1))
                    for dy,dx in d:
                        ny,nx=y1+dy,x1+dx
                        if 0<=ny<h and 0<=nx<w and g[ny][nx]==1 and (ny,nx)not in v:
                            v.add((ny,nx));s.append((ny,nx));Y.append(ny);X.append(nx)
                y0,y1=min(Y),max(Y);x0,x1=min(X),max(X)
                S={(i,j)for i in range(y0,y1+1)for j in range(x0,x1+1)if g[i][j]==9 and (i in(y0,y1) or j in(x0,x1))};q=list(S)
                while q:
                    y2,x2=q.pop()
                    for dy,dx in d:
                        ny,nx=y2+dy,x2+dx
                        if y0<=ny<=y1 and x0<=nx<=x1 and g[ny][nx]==9 and (ny,nx)not in S:S.add((ny,nx));q.append((ny,nx))
                if any(g[i][j]==9 and (i,j)not in S for i in range(y0,y1+1) for j in range(x0,x1+1)):
                    for y2,x2 in C:g[y2][x2]=8
    return g
