def p(g):
    C=set(sum(g,[]))
    def box(c):
        t=[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v==c]
        if not t:return 99
        xs,ys=zip(*t)
        return max(max(xs)-min(xs)+1,max(ys)-min(ys)+1)
    a=min(C,key=box)
    d=min(C-{a},key=lambda c:sum(r.count(c)for r in g))
    p=[[0]*25]+[[0]+r+[0]for r in g]+[[0]*25]
    s=[(i,j)for i in range(25)for j in range(25)if p[i][j]==a]
    xs,ys=zip(*s)
    si=min(xs);sj=min(ys);ei=max(xs);ej=max(ys)
    q=[r[sj:ej+1]for r in p[si:ei+1]]
    def rot(x):return [list(r)for r in zip(*x[::-1])]
    def fl(x):return [r[::-1]for r in x]
    T=[];r=q
    for _ in range(4):
        T+=r,fl(r);r=rot(r)
    for t in T:
        h=len(t);w=len(t[0])
        m=[[0 if v==a else d if v==d else -1 for v in row]for row in t]
        for i in range(25-h+1):
            for j in range(25-w+1):
                if all(m[x][y]<0 or p[i+x][j+y]==m[x][y] for x in range(h)for y in range(w)):
                    for x in range(h):p[i+x][j:j+w]=t[x]
    return[row[1:-1]for row in p[1:-1]]
