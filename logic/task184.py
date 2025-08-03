def p(g):
    h=len(g);w=len(g[0])
    R=[-1]+[i for i,r in enumerate(g)if not any(r)]+[h]
    C=[-1]+[i for i in range(w)if not any(r[i]for r in g)]+[w]
    o=[];m=len(C)-1
    for i in range(len(R)-1):
        x=[]
        for j in range(m):
            u=[]
            for r in g[R[i]+1:R[i+1]]:
                for v in r[C[j]+1:C[j+1]]:
                    if v and v not in u:u+=v,
            x+=u if m==1 else [u[0]]
        o+=x,
    return o
