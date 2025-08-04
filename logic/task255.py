def p(g):
    h=len(g);w=len(g[0])
    d=[[99]*w for _ in g];q=[]
    for i in range(h):
        for j in range(w):
            if g[i][j]:d[i][j]=0;q.append((i,j))
    p0=0
    while p0<len(q):
        i,j=q[p0];p0+=1
        for di in(-1,0,1):
            for dj in(-1,0,1):
                if di|dj:
                    ni=i+di;nj=j+dj
                    if 0<=ni<h and 0<=nj<w and d[ni][nj]>d[i][j]+1:
                        d[ni][nj]=d[i][j]+1;q.append((ni,nj))
    s=[[0]*w for _ in g]
    for i in range(h):
        for j in range(w):
            if g[i][j]==0 and all((0<=i+di<h and 0<=j+dj<w and g[i+di][j+dj]==0) or not(0<=i+di<h and 0<=j+dj<w) for di in(-1,0,1) for dj in(-1,0,1)):
                s[i][j]=1
    best=0;si=sj=0
    for i in range(h):
        for j in range(w):
            if s[i][j] and d[i][j]>best:best=d[i][j];si,sj=i,j
    if not best:return [r[:] for r in g]
    t=b=si;l=r=sj
    while 1:
        ch=0
        if l>0 and all(s[i][l-1] for i in range(t,b+1)):l-=1;ch=1
        if r<w-1 and all(s[i][r+1] for i in range(t,b+1)):r+=1;ch=1
        if t>0 and all(s[t-1][j] for j in range(l,r+1)):t-=1;ch=1
        if b<h-1 and all(s[b+1][j] for j in range(l,r+1)):b+=1;ch=1
        if not ch:break
    o=[r[:] for r in g]
    for i in range(t,b+1):
        for j in range(l,r+1):o[i][j]=3
    return o
