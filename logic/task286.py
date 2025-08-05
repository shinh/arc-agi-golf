def p(g):
    h=len(g);w=len(g[0]);c=[0]*10;R=range(10);M=9e9
    for r in g:
        for v in r:c[v]+=1
    f=lambda k:(c[k] or M,k);c0=min(R,key=f);c[c0]=M;c1=min(R,key=f)
    S=set();o=0
    for i,r in enumerate(g):
        for j,v in enumerate(r):
            if v==c0:o=(i,j);S.add((i,j))
            elif v==c1:S.add((i,j))
    nb=[0]*10
    for i,j in S:
        for di in(-1,0,1):
            for dj in(-1,0,1):
                if di or dj:
                    ni=i+di;nj=j+dj
                    if 0<=ni<h and 0<=nj<w and (ni,nj)not in S:
                        nb[g[ni][nj]]+=1
    c2=min(R,key=lambda k:(nb[k] or M,k))
    d=((1,0),(-1,0),(0,1),(0,-1))
    q=list(S);P=set()
    while q:
        x,y=q.pop()
        for dx,dy in d:
            nx,ny=x+dx,y+dy
            if 0<=nx<h and 0<=ny<w and (nx,ny)not in S and g[nx][ny]==c2:
                S.add((nx,ny));P.add((nx,ny));q.append((nx,ny))
    b=(o[0]+o[1])&1;T=(c0,c1)
    for i,j in P:g[i][j]=T[(i+j)&1^b]
    return g
