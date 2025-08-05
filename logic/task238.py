def p(g):
    h=len(g);w=len(g[0])
    bg=0
    v=[[0]*w for _ in g];R=0,0,0,0,0
    for y in range(h):
        for x in range(w):
            if g[y][x]==0 and not v[y][x]:
                q=[(y,x)];v[y][x]=1;cnt=0;sy=h;sx=w;ey=ex=0
                while q:
                    i,j=q.pop();cnt+=1;sy=min(sy,i);sx=min(sx,j);ey=max(ey,i);ex=max(ex,j)
                    for a,b in((1,0),(-1,0),(0,1),(0,-1)):
                        ni,nj=i+a,j+b
                        if 0<=ni<h and 0<=nj<w and g[ni][nj]==0 and not v[ni][nj]:
                            v[ni][nj]=1;q.append((ni,nj))
                if cnt==(ey-sy+1)*(ex-sx+1):R=max(R,(cnt,sy,ey,sx,ex))
    _,sy,ey,sx,ex=R
    r0=sy-1;c0=sx-1;r1=ey+1;c1=ex+1
    P=[r[c0:c1+1]for r in g[r0:r1+1]]
    H=len(P);W=len(P[0])
    v=[[0]*W for _ in P];B=[]
    for y in range(H):
        for x in range(W):
            if P[y][x] and not v[y][x]:
                q=[(y,x)];v[y][x]=1;c=[]
                while q:
                    i,j=q.pop();c.append((i,j))
                    for a,b in((1,0),(-1,0),(0,1),(0,-1)):
                        ni,nj=i+a,j+b
                        if 0<=ni<H and 0<=nj<W and P[ni][nj]==P[y][x] and not v[ni][nj]:
                            v[ni][nj]=1;q.append((ni,nj))
                B.append((P[y][x],c))
    ext=[(g[y][x],y,x)for y in range(h)for x in range(w)if g[y][x] and not(r0<=y<=r1 and c0<=x<=c1)]
    if ext:
        mi=min(y for _,y,_ in ext);mj=min(x for _,_,x in ext);C=[]
        for v,y,x in ext:
            i=y-mi+1;j=x-mj+1
            if 0<=i<H and 0<=j<W:P[i][j]=v;C.append((i,j))
        for y,x in C:
            ds=[min(abs(y-i)+abs(x-j)for i,j in c)for _,c in B];m=min(ds)
            if ds.count(m)==1:P[y][x]=B[ds.index(m)][0]
    return P
