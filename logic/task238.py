def p(g):
    h=len(g);w=len(g[0])
    d={}
    for r in g:
        for v in r:d[v]=d.get(v,0)+1
    bg=max(d,key=d.get)
    v=[[0]*w for _ in g];R=[]
    for y in range(h):
        for x in range(w):
            if g[y][x]==bg and not v[y][x]:
                q=[(y,x)];v[y][x]=1;c=[]
                while q:
                    i,j=q.pop();c.append((i,j))
                    for a,b in((1,0),(-1,0),(0,1),(0,-1)):
                        ni,nj=i+a,j+b
                        if 0<=ni<h and 0<=nj<w and g[ni][nj]==bg and not v[ni][nj]:
                            v[ni][nj]=1;q.append((ni,nj))
                ys=[i for i,_ in c];xs=[j for _,j in c]
                if len(c)==(max(ys)-min(ys)+1)*(max(xs)-min(xs)+1):R.append((len(c),min(ys),max(ys),min(xs),max(xs)))
    _,sy,ey,sx,ex=max(R)
    r0=sy-1;c0=sx-1;r1=ey+1;c1=ex+1
    P=[r[c0:c1+1]for r in g[r0:r1+1]]
    H=len(P);W=len(P[0])
    v=[[0]*W for _ in P];B=[]
    for y in range(H):
        for x in range(W):
            if P[y][x]!=bg and not v[y][x]:
                q=[(y,x)];v[y][x]=1;c=[]
                while q:
                    i,j=q.pop();c.append((i,j))
                    for a,b in((1,0),(-1,0),(0,1),(0,-1)):
                        ni,nj=i+a,j+b
                        if 0<=ni<H and 0<=nj<W and P[ni][nj]==P[y][x] and not v[ni][nj]:
                            v[ni][nj]=1;q.append((ni,nj))
                B.append((P[y][x],c))
    ext=[];mi=h;mj=w
    for y in range(h):
        for x in range(w):
            if not(r0<=y<=r1 and c0<=x<=c1) and g[y][x]!=bg:
                ext.append((g[y][x],y,x));mi=min(mi,y);mj=min(mj,x)
    P2=[r[:]for r in P];C=[]
    for v,y,x in ext:
        i=y-mi+1;j=x-mj+1
        if 0<=i<H and 0<=j<W:P2[i][j]=v;C.append((i,j))
    for y,x in C:
        ds=[min(abs(y-i)+abs(x-j)for i,j in c)for _,c in B];m=min(ds)
        if ds.count(m)==1:P2[y][x]=B[ds.index(m)][0]
    return P2
