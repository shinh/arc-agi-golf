def p(g):
    w=h=23
    C=set(sum(g,[]))
    def box(c):
        t=[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v==c]
        if not t:return 99
        xs,ys=zip(*t)
        return max(max(xs)-min(xs)+1,max(ys)-min(ys)+1)
    a=min(C,key=box)
    cnt={c:sum(r.count(c)for r in g)for c in C}
    b=0
    d=min([c for c in C if c!=a],key=cnt.get)
    p=[[b]*(w+2)for _ in range(h+2)]
    for i,r in enumerate(g):
        for j,v in enumerate(r):p[i+1][j+1]=v
    s=[(i,j)for i in range(h+2)for j in range(w+2)if p[i][j]==a]
    si=min(i for i,j in s);sj=min(j for i,j in s);ei=max(i for i,j in s);ej=max(j for i,j in s)
    q=[r[sj:ej+1]for r in p[si:ei+1]]
    def rot(x):return [list(r)for r in zip(*x[::-1])]
    def fl(x):return [r[::-1]for r in x]
    T=[];r=q
    for _ in range(4):
        T+=r,fl(r);r=rot(r)
    U=[]
    [U.append(t)for t in T if t not in U]
    H=W=25
    for t in U:
        mh=len(t);mw=len(t[0])
        m=[[0 if v==a else d if v==d else None for v in row]for row in t]
        for i in range(H-mh+1):
            for j in range(W-mw+1):
                if all(m[x][y] is None or p[i+x][j+y]==m[x][y] for x in range(mh)for y in range(mw)):
                    for x in range(mh):
                        for y in range(mw):
                            p[i+x][j+y]=t[x][y]
    return[row[1:-1]for row in p[1:-1]]
