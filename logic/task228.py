def p(g):
    w=h=T=L=10;B=R=0
    for y in range(h):
        for x in range(w):
            if g[y][x]:
                if y<T:T=y
                if y>B:B=y
                if x<L:L=x
                if x>R:R=x
    a,b,c,d=g[T+1][L+1],g[T+1][R-1],g[B-1][L+1],g[B-1][R-1]
    for y in range(T+1,B):g[y][L+1:R]=[0]*(R-L-1)
    g[T-1][L-1]=d;g[T-1][R+1]=c;g[B+1][L-1]=b;g[B+1][R+1]=a
    return g
