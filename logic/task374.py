def p(g):
    h=len(g);w=len(g[0])
    out=[r[:] for r in g];seen=[[0]*w for _ in g];objs=[]
    for i in range(h):
        for j in range(w):
            if g[i][j]==0 or seen[i][j]:continue
            q=[(i,j)];seen[i][j]=1;cell=[]
            while q:
                x,y=q.pop();cell.append((x,y))
                for dx,dy in((1,0),(-1,0),(0,1),(0,-1)):
                    nx,ny=x+dx,y+dy
                    if 0<=nx<h and 0<=ny<w and g[nx][ny] and not seen[nx][ny]:
                        seen[nx][ny]=1;q.append((nx,ny))
            objs.append(cell)
    for o in objs:
        for x,y in o: out[x][y]=4
    big=max(objs,key=len);small=min(objs,key=len)
    for x,y in big: out[x][y]=1
    for x,y in small: out[x][y]=2
    return out
