def p(g):
    H=len(g);W=len(g[0]);s=[[0]*W for _ in g];R=[]
    for i in range(H):
        for j in range(W):
            if s[i][j]:continue
            c=g[i][j];S=[(i,j)];s[i][j]=1;C=[]
            while S:
                x,y=S.pop();C.append((x,y))
                for dx,dy in((1,0),(-1,0),(0,1),(0,-1)):
                    nx,ny=x+dx,y+dy
                    if 0<=nx<H and 0<=ny<W and not s[nx][ny] and g[nx][ny]==c:
                        s[nx][ny]=1;S.append((nx,ny))
            r0=min(x for x,_ in C);r1=max(x for x,_ in C)
            c0=min(y for _,y in C);c1=max(y for _,y in C)
            if r1-r0>1 and c1-c0>1:
                B={(x,y)for x in range(r0,r1+1)for y in range(c0,c1+1)if x in{r0,r1}or y in{c0,c1}}
                if set(C)==B:R.append((c,r0,c0,r1,c1))
    col={}
    for c,*_ in R:col[c]=col.get(c,0)+1
    col=min(col,key=lambda k:(col[k],k))
    for c,r0,c0,r1,c1 in R:
        if c==col:
            ring=[(x-r0,y-c0)for x in range(r0,r1+1)for y in range(c0,c1+1)if x in{r0,r1}or y in{c0,c1}]
            ih=r1-r0-1;iw=c1-c0-1;break
    res=[r[:] for r in g]
    for i in range(H-ih+1):
        for j in range(W-iw+1):
            if all(g[i+x][j+y]==0 for x in range(ih)for y in range(iw)if x in{0,ih-1}or y in{0,iw-1}):
                for x,y in ring:
                    a=i-1+x;b=j-1+y
                    if 0<=a<H and 0<=b<W:res[a][b]=col
    return res
