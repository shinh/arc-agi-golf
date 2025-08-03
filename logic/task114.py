def p(g):
    h=len(g);w=len(g[0])
    o=[[0]*(w+2) for _ in range(h+2)]
    o[0][1:-1]=g[0];o[-1][1:-1]=g[-1]
    for i,r in enumerate(g):
        o[i+1][1:-1]=r;o[i+1][0]=r[0];o[i+1][-1]=r[-1]
    return o
