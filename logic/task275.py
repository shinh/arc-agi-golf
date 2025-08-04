def p(g):
    h=len(g);w=len(g[0])
    if w//2==h:
        A=[r[:w//2] for r in g];B=[r[w//2:] for r in g]
    else:
        A=g[:h//2];B=g[h//2:]
    def pal(x):
        s=set();[s.update(r) for r in x];return s
    if len(pal(A))<len(pal(B)):pat,lay=A,B
    else:pat,lay=B,A
    bg=(pal(pat)&pal(lay)).pop();n=len(pat)
    pts=[(i,j)for i in range(n)for j in range(n)if pat[i][j]!=bg]
    cells=[(lay[i][j],i,j)for i in range(n)for j in range(n)if lay[i][j]!=bg]
    o=[[bg]*(n*n)for _ in range(n*n)]
    for v,i,j in cells:
        for a,b in pts:o[i*n+a][j*n+b]=v
    return o
