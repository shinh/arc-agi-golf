def p(g):
    h=len(g);w=len(g[0])
    N8=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
    N4=N8[:4]
    def objs(ds):
        seen=[[0]*w for _ in g];O=[]
        for i in range(h):
            for j in range(w):
                if g[i][j] and not seen[i][j]:
                    col=g[i][j];q=[(i,j)];seen[i][j]=1;c=[]
                    while q:
                        x,y=q.pop();c.append((x,y))
                        for dx,dy in ds:
                            nx,ny=x+dx,y+dy
                            if 0<=nx<h and 0<=ny<w and not seen[nx][ny] and g[nx][ny]==col:
                                seen[nx][ny]=1;q.append((nx,ny))
                    O.append((col,c))
        return O
    L=0
    for col,c in objs(N8):
        if all(x-y==c[0][0]-c[0][1] for x,y in c):L=col
    out=[r[:] for r in g]
    for col,c in objs(N4):
        if col==L and len(c)==1:continue
        rs=[i for i,_ in c];cs=[j for _,j in c]
        ul=(min(rs),min(cs));ur=(min(rs),max(cs));ll=(max(rs),min(cs))
        if ur in c:
            st=(ur[0]-1,ur[1]+1);col=g[ul[0]+1][ul[1]]
        else:
            st=(ll[0]+1,ll[1]-1);col=g[ul[0]][ul[1]+1]
        for x,y in c:out[x][y]=0
        x,y=st
        while 0<=x<h and 0<=y<w:out[x][y]=col;x-=1;y-=1
        x,y=st
        while 0<=x<h and 0<=y<w:out[x][y]=col;x+=1;y+=1
    return out
