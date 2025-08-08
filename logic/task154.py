def p(g):
    g=[r for r in g]
    b=[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v==2]
    j0=min(j for _,j in b);j1=max(j for _,j in b);c=(j0+j1)//2
    t=any(j==c for _,j in b)
    if t:
        g=[list(r)for r in zip(*g)]
        b=[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v==2]
        j0=min(j for _,j in b);j1=max(j for _,j in b)
    L,R=j0,j1
    r=[(i,j)for i,row in enumerate(g)for j,v in enumerate(row)if v==5]
    A=[(i,j)for i,j in r if j<L];B=[(i,j)for i,j in r if j>R]
    def f(s,a,l):
        if not s:return[]
        mj=min(j for _,j in s);Mj=max(j for _,j in s)
        s=[(i,mj+Mj-j)for i,j in s]
        d=l-(mj if a else Mj)
        return[(i,j+d)for i,j in s]
    nl=f(A,1,L+2);nr=f(B,0,R-2)
    for i,j in r:g[i][j]=0
    for i,j in nl+nr:g[i][j]=5
    if t:g=[list(r)for r in zip(*g)]
    return g

