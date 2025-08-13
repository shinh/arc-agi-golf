def p(g):
    f=sum(g,[])
    c=max(f,key=f.count)
    print('zzz',c)
    show(g,"in")
    for i in range(120):
        m=max(r.count(c)for r in g)
        if g[0].count(c)<m-4:g=g[1:]
        g=[*map(list,zip(*g[::-1]))]

    show(g,"crop")
    assert len(set(sum(g,[])))==2

    pts=[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v!=c]
    H=len(g);W=len(g[0])
    for i,j in pts:
        for k in range(H):g[k][j]=g[i][j]
        for k in range(W):g[i][k]=g[i][j]
    return g
