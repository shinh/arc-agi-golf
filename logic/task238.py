def p(g):
    h=len(g);w=len(g[0]);D=1,0,-1,0,1
    v=[[0]*w for _ in g];R=0,0,0,0,0
    for y in range(h):
        for x in range(w):
            if g[y][x]<1 and not v[y][x]:
                q=[(y,x)];v[y][x]=1;n=0;a=h;c=w;b=e=0
                while q:
                    i,j=q.pop();n+=1;a=min(a,i);c=min(c,j);b=max(b,i);e=max(e,j)
                    for k in range(4):
                        ni=i+D[k];nj=j+D[k+1]
                        if 0<=ni<h and 0<=nj<w and g[ni][nj]<1 and not v[ni][nj]:
                            v[ni][nj]=1;q.append((ni,nj))
                if n==(b-a+1)*(e-c+1):R=max(R,(n,a,b,c,e))
    _,a,b,c,e=R
    P=[r[c-1:e+2]for r in g[a-1:b+2]]
    H=len(P);W=len(P[0]);B={}
    for y,r in enumerate(P):
        for x,k in enumerate(r):
            if k:B.setdefault(k,[]).append((y,x))
    ext=[(g[y][x],y,x)for y in range(h)for x in range(w)if g[y][x] and not(a-1<=y<=b+1 and c-1<=x<=e+1)]
    if ext:
        mi=min(y for _,y,_ in ext);mj=min(x for _,_,x in ext);C=[]
        for k,y,x in ext:
            i=y-mi+1;j=x-mj+1
            if 0<=i<H and 0<=j<W:P[i][j]=k;C.append((i,j))
        I=list(B.items())
        for y,x in C:
            ds=[min(abs(y-i)+abs(x-j)for i,j in c)for _,c in I];m=min(ds)
            if ds.count(m)<2:P[y][x]=I[ds.index(m)][0]
    return P
