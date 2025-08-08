def p(g):
    h=len(g);w=len(g[0])
    f=sum(g,[]);c={}
    for v in f:c[v]=c.get(v,0)+1
    lt=min(c,key=c.get)
    out=[r for r in g];seen=[[0]*w for _ in g]
    for i in range(h):
        for j in range(w):
            if g[i][j] or seen[i][j]:continue
            q=[(i,j)];seen[i][j]=1;cell=[]
            while q:
                x,y=q.pop();cell.append((x,y))
                for dx,dy in((1,0),(-1,0),(0,1),(0,-1)):
                    nx,ny=x+dx,y+dy
                    if 0<=nx<h and 0<=ny<w and g[nx][ny]==0 and not seen[nx][ny]:
                        seen[nx][ny]=1;q.append((nx,ny))
            xs=[x for x,_ in cell];ys=[y for _,y in cell]
            m1,m2=min(xs),min(ys);M1,M2=max(xs),max(ys)
            if len(cell)==(M1-m1+1)*(M2-m2+1):
                chk=[(m1-2,m2-1),(m1-1,m2-2),(m1-2,M2+1),(m1-1,M2+2),(M1+2,m2-1),(M1+1,m2-2),(M1+2,M2+1),(M1+1,M2+2)]
                if all(not(0<=x<h and 0<=y<w and g[x][y]==lt) for x,y in chk):
                    for x,y in cell: out[x][y]=4
    return out
