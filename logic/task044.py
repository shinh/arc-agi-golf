def p(g):
    h=len(g);w=len(g[0]);r=[i[:] for i in g]
    for c in {v for r0 in g for v in r0}-{0,5}:
        P=[(i,j)for i,r0 in enumerate(g)for j,v in enumerate(r0)if v==c]
        y0=min(i for i,_ in P);x0=min(j for _,j in P)
        S=[(i-y0,j-x0)for i,j in P]
        hh=max(i for i,_ in S)+1;ww=max(j for _,j in S)+1
        R=range(h//2,h-hh+1)if y0<h//2 else range(h//2-hh+1)
        f=0
        for y in R:
            for x in range(w-ww+1):
                if all(g[y+dy][x+dx]==0 for dy,dx in S)and all((not y or g[y-1][x+j]==5)and(y+hh==h or g[y+hh][x+j]==5)for j in range(ww)):
                    for dy,dx in S:r[y+dy][x+dx]=c
                    for i,j in P:r[i][j]=0
                    f=1;break
            if f:break
    return r
