def p(g):
    sx=g[1][0]<1
    sy=g[0][1]<1
    c=g[1][1]
    n=len(set(sum(g,[])))-1
    g=[[cn for c in rn for cn in[c]*n] for r in g for rn in [r]*n]

    def put_red(y,x):
        if 0<=y<len(g) and 0<=x<len(g[0]) and g[y][x]<1:
            g[y][x]=2

    for i in range(n):
        put_red(sy*n-i-1,sx*n-i-1)
        put_red(sy*n-i-1,sx*n+2*n+i)
        put_red(sy*n+2*n+i,sx*n-i-1)
        put_red(sy*n+2*n+i,sx*n+2*n+i)

    return g
