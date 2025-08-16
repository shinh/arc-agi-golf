def p(g):
    # find colored rectangle, clear inside, push inner corners outward
    T=L=9;B=R=0
    for y in range(10):
        for x in range(10):
            if g[y][x]:T=min(T,y);B=max(B,y);L=min(L,x);R=max(R,x)
    t=g[T+1][:];b=g[B-1][:]
    for r in g[T+1:B]:r[L+1:R]=[0]*(R-L-1)
    g[T-1][L-1],g[T-1][R+1],g[B+1][L-1],g[B+1][R+1]=b[R-1],b[L+1],t[R-1],t[L+1]
    return g
