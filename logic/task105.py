def p(g):
    # outline rare color region with 2 and fill lines
    a=min(f:=sum(g,[]),key=f.count);P=[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v==a]
    if P:
        I,J=zip(*P);t,B=min(I),max(I);l,R=min(J),max(J)
        h,v=range(l,R+1),range(t,B+1)
        for i in t,B:
            for j in h:g[i][j]=g[i][j]or 2
        for i in v:
            for j in l,R:g[i][j]=g[i][j]or 2
        S,T={i for i,j in P if t<i<B and l<j<R},{j for i,j in P if t<i<B and l<j<R}
        if len(T)*len(v)>len(S)*len(h):
            for i in S:
                for j in h:g[i][j]=g[i][j]or 2
        else:
            for j in T:
                for i in v:g[i][j]=g[i][j]or 2
    return g

