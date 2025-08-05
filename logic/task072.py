def p(g):
    if len({r[6]for r in g})==1:a=[r[:6]for r in g];b=[r[7:]for r in g]
    else:a=g[:2];b=g[3:]
    c=[next(v for v in sum(t,[]) if v)for t in(a,b)]
    s=[{(i,j)for i,r in enumerate(t)for j,v in enumerate(r)if v==c[k]}for k,t in enumerate((a,b))]
    R=s[0]^s[1];o=[[0]*len(a[0])for _ in a]
    for i,j in R:o[i][j]=3
    return o
