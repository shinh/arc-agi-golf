def p(g):
    # outline rare color region with 2 and fill lines
    P=[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v==1]
    if P:
        I,J=zip(*P);t,B=min(I),max(I);l,R=min(J),max(J)
        h,v=range(l,R+1),range(t,B+1)
        S,T={i for i,j in P if t<i<B and l<j<R},{j for i,j in P if t<i<B and l<j<R}
        f=len(T)*len(v)>len(S)*len(h)
        for i in v:
            for j in h:
                if i in(t,B)or j in(l,R)or i in S and f or j in T and f<1:g[i][j]=g[i][j]or 2
    return g

