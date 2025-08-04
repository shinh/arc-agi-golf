def p(g):
    h=len(g);w=len(g[0]);s=set();B=[]
    for i in range(h):
        for j in range(w):
            if (i,j)in s:continue
            c=g[i][j];q=[(i,j)];s.add((i,j));t=[]
            while q:
                x,y=q.pop();t.append((x,y))
                for a,b in(1,0),(-1,0),(0,1),(0,-1):
                    u,v=x+a,y+b
                    if 0<=u<h and 0<=v<w and g[u][v]==c and(u,v)not in s:s.add((u,v));q.append((u,v))
            if len(t)>len(B):B=t;col=c
    rs=[x for x,_ in B];cs=[y for _,y in B]
    x=[r[min(cs):max(cs)+1]for r in g[min(rs):max(rs)+1]]
    for _ in range(32):
        x=[list(r)for r in zip(*x[::-1])]
        if len(x[0])-2>sum(v==col for v in x[0]):x=x[1:]
    f=[v for r in x for v in r];c=min(set(f),key=f.count)
    pts=[(i,j)for i,r in enumerate(x)for j,v in enumerate(r)if v==c]
    H=len(x);W=len(x[0])
    for i,j in pts:
        for k in range(H):x[k][j]=c
        for k in range(W):x[i][k]=c
    return x
