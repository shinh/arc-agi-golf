def p(g):
    c=[r[2:-2]for r in g[2:-2]];h=len(g)
    B=[[v for j,v in enumerate(r) if len({g[i][j]for i in range(h)})>1]for r in g if len(set(r))>1]
    b=B[0][1];t=(set(v for r in c for v in r)-{b}).pop()
    q=((g[0][0],g[0][-1]),(g[-1][0],g[-1][-1]));H=len(c)//2;W=len(c[0])//2
    for i,r in enumerate(c):
        for j,v in enumerate(r):
            if v==t:r[j]=q[i>=H][j>=W]
    return c
