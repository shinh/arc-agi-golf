def p(g):
    C=set(sum(g,[]))
    def box(c):
        t=[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v==c]
        if not t:return 99
        xs,ys=zip(*t)
        return max(max(xs)-min(xs)+1,max(ys)-min(ys)+1)
    a=min(C,key=box)
    d=min(C-{a},key=lambda c:sum(v==c for r in g for v in r))
    p=[[0]*25]+[[0]+r+[0]for r in g]+[[0]*25]
    xs,ys=zip(*((i,j)for i in range(25)for j in range(25)if p[i][j]==a))
    si=min(xs);sj=min(ys);ei=max(xs);ej=max(ys)
    q=[r[sj:ej+1]for r in p[si:ei+1]]
    r=q
    for _ in range(4):
        for t in r,[row[::-1]for row in r]:
            h=len(t);w=len(t[0]);m=[[d*(v==d)-(v!=a)*(v!=d)for v in row]for row in t]
            for i in range(26-h):
                for j in range(26-w):
                    if all(m[x][y]<0 or p[i+x][j+y]==m[x][y] for x in range(h)for y in range(w)):
                        for x in range(h):p[i+x][j:j+w]=t[x]
        r=[list(s)for s in zip(*r[::-1])]
    return[row[1:-1]for row in p[1:-1]]
