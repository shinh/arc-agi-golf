def p(g):
    # drop blocks and stack them
    h=len(g);w=len(g[0]);S=[];M=R=[]
    for y in range(h):
        for x in range(w):
            if g[y][x]>4:
                q=[(y,x)];g[y][x]=0
                for i,j in q:
                    for u,v in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
                        if h>u>=0<w>v>=0 and g[u][v]>4:g[u][v]=0;q+=[(u,v)]
                Y,X=zip(*q);a=min(Y);b=min(X);S+=[([(i-a,j-b)for i,j in q],max(Y)-a+1,max(X)-b+1)]
    S.sort(key=lambda t:-len(t[0]))
    def F(i):
        nonlocal M,R
        if i==len(S):
            t=[(i,j)for i in range(h)for j in range(w)if g[i][j]]
            if not M or t<M:M,R=t,[r[:]for r in g]
            return
        T,H,W=S[i]
        for x in range(w-W+1):
            y=h-H
            while y and all(not g[y+dy-1][x+dx] for dy,dx in T):y-=1
            if all(not g[y+dy][x+dx] for dy,dx in T):
                for dy,dx in T:g[y+dy][x+dx]=1
                F(i+1)
                for dy,dx in T:g[y+dy][x+dx]=0
    F(0)
    return R
