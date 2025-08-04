def p(g):
    B=max(range(10),key=lambda c:sum(r.count(c)for r in g))
    d=lambda x:[list(r)for r in zip(*x)]
    c=lambda x:[list(r)for r in zip(*(r[::-1]for r in x[::-1]))]
    for f in (lambda x:x,d,c,lambda x:x[::-1]):
        G=f(g)
        if len({*G[0]})==1 and G[0][0]!=B:break
    h=len(G);w=len(G[0]);o=[r[:] for r in G];S=[]
    for y in range(h):
        for x in range(w):
            if G[y][x]==5:
                q=[(y,x)];G[y][x]=0;c=[]
                while q:
                    i,j=q.pop();o[i][j]=0;c.append((i,j))
                    for u,v in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
                        if 0<=u<h and 0<=v<w and G[u][v]==5:G[u][v]=0;q.append((u,v))
                a=min(y for y,_ in c);b=min(x for _,x in c)
                S.append(([(y-a,x-b)for y,x in c],max(y for y,_ in c)-a+1,max(x for _,x in c)-b+1))
    S.sort(key=lambda t:(-len(t[0]),-t[2]))
    M=R=None
    def F(i,o):
        nonlocal M,R
        if i==len(S):
            t=tuple((i,j)for i,r in enumerate(o)for j,v in enumerate(r)if v)
            if M is None or t<M:M,R=t,[r[:]for r in o]
            return
        T,H,W=S[i]
        for x in range(w-W+1):
            y=h-H
            while y and all(o[y+dy-1][x+dx]==0 for dy,dx in T):y-=1
            if all(o[y+dy][x+dx]==0 for dy,dx in T):
                n=[r[:] for r in o]
                for dy,dx in T:n[y+dy][x+dx]=1
                F(i+1,n)
    F(0,o)
    return f(R)
