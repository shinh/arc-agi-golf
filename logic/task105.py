def p(g):
    from collections import Counter as C
    c=C(sum(g,[]));a=min(c,key=c.get);b=max(c,key=c.get)
    P=[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v==a]
    if not P:return g
    I,J=zip(*P);t,B=min(I),max(I);l,R=min(J),max(J)
    G=[r[:]for r in g]
    for i in range(t,B+1):
        for j in range(l,R+1):
            if(i in(t,B)or j in(l,R))and G[i][j]==b:G[i][j]=2
    Q=[(i,j)for i,j in P if t<i<B and l<j<R]
    if Q:
        Rw={i for i,_ in Q};Cl={j for _,j in Q}
        if len(Cl)<=len(Rw):
            for j in Cl:
                for i in range(t,B+1):
                    if G[i][j]==b:G[i][j]=2
        else:
            for i in Rw:
                for j in range(l,R+1):
                    if G[i][j]==b:G[i][j]=2
    return G
