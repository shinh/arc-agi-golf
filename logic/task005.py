def p(g):
    n=len(g);m=len(g[0]);s=n//3
    c=[r[s:2*s] for r in g[s:2*s]]
    o=[[0]*m for _ in range(n)]
    for gy in range(3):
        for gx in range(3):
            b=[r[:] for r in c]
            if gy==0:b=b[::-1]
            if gx==0:b=[r[::-1] for r in b]
            for y in range(s):
                for x in range(s):
                    v=b[y][x]
                    if v:o[gy*s+y][gx*s+x]=v
    return o
