def p(g):
    h=len(g);w=len(g[0])
    R=[i for i,r in enumerate(g)if all(v==5 for v in r)]
    C=[j for j in range(w)if all(g[y][j]==5 for y in range(h))]
    a=len(R)//2;b=len(C)//2
    for y in range(R[0]):g[y][:C[0]]=[1]*C[0]
    for y in range(R[a-1]+1,R[a]):g[y][C[b-1]+1:C[b]]=[2]*(C[b]-C[b-1]-1)
    for y in range(R[-1]+1,h):g[y][C[-1]+1:]=[3]*(w-C[-1]-1)
    return g
