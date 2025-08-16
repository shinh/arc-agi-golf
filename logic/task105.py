def p(g):
    # outline rare color region with 2 and fill lines
    a=min(f:=sum(g,[]),key=f.count);P=[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v==a]
    if not P:return g
    I,J=zip(*P);t,B=min(I),max(I);l,R=min(J),max(J)
    for i in range(t,B+1):
        for j in range(l,R+1):
            if(i in(t,B)or j in(l,R))and g[i][j]<1:g[i][j]=2
    S={i for i,j in P if t<i<B and l<j<R};T={j for i,j in P if t<i<B and l<j<R}
    if len(T)*(B-t+1)>len(S)*(R-l+1):
        for i in S:
            for j in range(l,R+1):
                if g[i][j]<1:g[i][j]=2
    else:
        for j in T:
            for i in range(t,B+1):
                if g[i][j]<1:g[i][j]=2
    return g

