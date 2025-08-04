def p(g):
    pts=[(i,j,v)for i,r in enumerate(g)for j,v in enumerate(r)if v]
    (r1,c1,v1),(r2,c2,v2)=pts
    t=abs(r1-r2)<abs(c1-c2)
    if t:
        g=[list(r)for r in zip(*g)];r1,c1,r2,c2=c1,r1,c2,r2
    if r1>r2:r1,c1,v1,r2,c2,v2=r2,c2,v2,r1,c1,v1
    m=(r1+r2)//2;c=c1
    for i in range(r1,r2+1):g[i][c]=v2
    for i in range(r1,m+1):g[i][c]=v1
    for d in(-2,2):g[m][c+d]=v1;g[m+1][c+d]=v2
    for j in range(c-2,c+3):g[m-1][j]=v1;g[m+2][j]=v2
    g[m][c]=g[m+1][c]=0
    if t:g=[list(r)for r in zip(*g)]
    return g
