def p(g):
    t=lambda x:[list(r)for r in zip(*x)]
    r=lambda x:[list(r)for r in zip(*(q[::-1]for q in x[::-1]))]
    s=g
    for f in (lambda x:x,t,r,lambda x:x[::-1]):
        g=f(s)
        if len({*g[0]})==1 and g[0][0]:break
    h=len(g);w=len(g[0]);S=[]
    for y in range(h):
        for x in range(w):
            if g[y][x]==5:
                q=[(y,x)];g[y][x]=0;c=[]
                while q:
                    i,j=q.pop();c.append((i,j))
                    for u,v in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
                        if 0<=u<h and 0<=v<w and g[u][v]==5:g[u][v]=0;q.append((u,v))
                Y,X=zip(*c);a=min(Y);b=min(X)
                S.append(([(i-a,j-b)for i,j in c],max(Y)-a+1,max(X)-b+1))
    S.sort(key=lambda t:(-len(t[0]),-t[2]))
    M=R=None
    def F(i):
        nonlocal M,R,g
        if i==len(S):
            T=tuple((i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v)
            if M is None or T<M:M,R=T,[r[:]for r in g]
            return
        T,H,W=S[i]
        for x in range(w-W+1):
            y=h-H
            while y and all(g[y+dy-1][x+dx]==0 for dy,dx in T):y-=1
            if all(g[y+dy][x+dx]==0 for dy,dx in T):
                for dy,dx in T:g[y+dy][x+dx]=1
                F(i+1)
                for dy,dx in T:g[y+dy][x+dx]=0
    F(0)
    return f(R)

