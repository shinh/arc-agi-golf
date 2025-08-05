def p(g):
    h=w=5;cs={v for r in g for v in r};k=len(cs)-1
    G=[[g[i//k][j//k] for j in range(5*k)] for i in range(5*k)]
    best=bg=None;area=1e9;box=None
    for c in cs:
        pts=[(i,j) for i in range(h) for j in range(w) if g[i][j]==c]
        if not pts:continue
        mi=min(i for i,j in pts);ma=max(i for i,j in pts)
        mj=min(j for i,j in pts);mx=max(j for i,j in pts)
        ring={(i,mj-1) for i in range(mi-1,ma+2)}|{(i,mx+1) for i in range(mi-1,ma+2)}|{(mi-1,j) for j in range(mj-1,mx+2)}|{(ma+1,j) for j in range(mj-1,mx+2)}
        cols={g[i][j] for i,j in ring if 0<=i<h and 0<=j<w}
        if len(cols)==1:
            a=(ma-mi+1)*(mx-mj+1)
            if a<area:
                area=a;best=c;bg=cols.pop();box=(mi,ma,mj,mx)
    mi,ma,mj,mx=box
    mi*=k;ma=(ma+1)*k-1;mj*=k;mx=(mx+1)*k-1
    H=W=5*k
    def draw(i,j,di,dj):
        i+=di;j+=dj
        while 0<=i<H and 0<=j<W:
            if G[i][j]==bg:G[i][j]=2
            i+=di;j+=dj
    draw(mi,mj,-1,-1);draw(mi,mx,-1,1);draw(ma,mj,1,-1);draw(ma,mx,1,1)
    return G
