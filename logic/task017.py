def p(g):
    w=h=21;m=10**9
    for k in range(1,h):
        c=sum(a and b and a!=b for i in range(h-k) for a,b in zip(g[i],g[i+k]))
        if c<m:m=c;K=k
        if c==0:break
    k=K
    t=[[0]*w for _ in range(k)]
    for i,r in enumerate(g):
        for j,v in enumerate(r):
            if v:t[i%k][j]=v
    for a in t:
        for b in t:
            if all(x==y or 0 in (x,y) for x,y in zip(a,b)):
                for i,(x,y) in enumerate(zip(a,b)):
                    if not x:a[i]=y
        for l in range(1,w+1):
            b=a[:l];ok=1
            for i in range(l,w,l):
                for j,v in enumerate(a[i:i+l]):
                    u=b[j]
                    if u and v and u!=v:ok=0;break
                    if v and not u:b[j]=v
                if not ok:break
            if ok:
                for i in range(w):a[i]=b[i%l]
                break
    return [t[i%k] for i in range(h)]
