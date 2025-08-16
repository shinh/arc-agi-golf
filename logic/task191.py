def p(g):
    # copy the smallest-box color wherever rare-color markers fit
    s=sum(g,[]);C=set(s)
    def box(c):
        x,y=zip(*((i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v==c))
        return max(max(x)-min(x),max(y)-min(y))+1
    a=min(C,key=box)
    d=min(C-{a},key=s.count)
    N=25
    p=[[0]*N]+[[0]+r+[0]for r in g]+[[0]*N]
    x,y=zip(*((i,j)for i in range(N)for j in range(N)if p[i][j]==a))
    q=[r[min(y):max(y)+1]for r in p[min(x):max(x)+1]]
    r=q
    for _ in range(4):
        for t in r,[row[::-1]for row in r]:
            h=len(t);w=len(t[0]);m=[[d*(v==d)-(v!=a)*(v!=d)for v in row]for row in t]
            for i in range(N+1-h):
                for j in range(N+1-w):
                    if all(m[x][y]<0 or p[i+x][j+y]==m[x][y]for x in range(h)for y in range(w)):
                        for x in range(h):p[i+x][j:j+w]=t[x]
        r=[list(s)for s in zip(*r[::-1])]
    return[row[1:-1]for row in p[1:-1]]
