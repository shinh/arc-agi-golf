def p(g):
    d={}
    for r in g:
        for v in r:d[v]=d.get(v,0)+1
    b=max(d,key=d.get)
    c={}
    for i,r in enumerate(g):
        for j,v in enumerate(r):
            if v!=b:c.setdefault(v,set()).add((i,j))
    def F(s):
        r=set(s);o=[]
        while r:
            q={r.pop()};c=set(q)
            while q:
                x,y=q.pop()
                for u,v in((1,0),(-1,0),(0,1),(0,-1)):
                    t=(x+u,y+v)
                    if t in r:r.remove(t);q.add(t);c.add(t)
            o+=[c]
        return o
    def N(z):
        mi=min(i for i,j in z);mj=min(j for i,j in z)
        return {(i-mi,j-mj) for i,j in z}
    def V(z):
        mj=min(j for i,j in z);M=max(j for i,j in z);d=mj+M
        return {(i,d-j) for i,j in z}
    def H(z):
        mi=min(i for i,j in z);M=max(i for i,j in z);d=mi+M
        return {(d-i,j) for i,j in z}
    def D(z):
        a=min(i for i,j in z);b=min(j for i,j in z)
        return {(j-b+a,i-a+b) for i,j in z}
    def B(z):
        t={p for _,p in z}
        mi=min(i for i,j in t);mj=min(j for i,j in t)
        return ((mi+1,mj)in t)+((mi,mj+1)in t)
    a=[]
    for v,s in c.items():
        mx=max(max(y for x,y in q)-min(y for x,y in q)+1 for q in F(s))
        xs,ys=zip(*s)
        a+=[[v,s,max(max(xs)-min(xs),max(ys)-min(ys))+1+mx]]
    a.sort(key=lambda x:-x[2])
    P=[]
    for v,s,_ in a:
        wrap=lambda z:frozenset({(v,p) for p in z})
        f={wrap(s)}
        f|={wrap(V(s))}
        f|={wrap(V(D(V(s))))}
        f|={wrap(H(s))}
        best=max(f,key=B)
        P+=[(v,N({p for _,p in best}))]
    n=len(P);e=n if any(len(s)==1 for s in c.values()) else n+1;m=2*e-1
    o=[[b]*m for _ in range(m)]
    pts=[]
    for k,(v,s) in enumerate(P):
        for i,j in s:
            i+=k;j+=k
            if 0<=i<m and 0<=j<m:o[i][j]=v;pts+=[(v,i,j)]
    R=lambda G:[list(r) for r in zip(*G[::-1])]
    for _ in range(3):
        o=R(o)
        for v,i,j in pts:o[i][j]=v
    return o
