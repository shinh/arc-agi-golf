def p(g):
    h=len(g);w=len(g[0]);c={}
    for r in g:
        for v in r:c[v]=c.get(v,0)+1
    a=sorted(c,key=lambda k:(c[k],k));c0,c1=a[0],a[1]
    S=set();o=None
    for i,r in enumerate(g):
        for j,v in enumerate(r):
            if v==c0:o=(i,j);S.add((i,j))
            elif v==c1:S.add((i,j))
    nb={}
    for i,j in S:
        for di in(-1,0,1):
            for dj in(-1,0,1):
                if di or dj:
                    ni=i+di;nj=j+dj
                    if 0<=ni<h and 0<=nj<w and (ni,nj)not in S:
                        v=g[ni][nj];nb[v]=nb.get(v,0)+1
    c2=min(nb,key=lambda k:(nb[k],k))
    dirs=[(1,0),(-1,0),(0,1),(0,-1)]
    P=set();seen=set()
    for i in range(h):
        for j in range(w):
            if g[i][j]==c2 and (i,j)not in seen:
                q=[(i,j)];seen.add((i,j));comp=[];adj=False
                while q:
                    x,y=q.pop();comp.append((x,y))
                    for dx,dy in dirs:
                        nx,ny=x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w:
                            if (nx,ny)in S:adj=True
                            elif g[nx][ny]==c2 and (nx,ny)not in seen:
                                seen.add((nx,ny));q.append((nx,ny))
                if adj:P.update(comp)
    oi,oj=o
    for i,j in P:
        g[i][j]=c0 if (abs(i-oi)+abs(j-oj))%2<1 else c1
    return g
