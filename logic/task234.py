def p(g):
    from collections import Counter
    h=len(g);w=len(g[0])
    bg=Counter(sum(g,[])).most_common(1)[0][0]
    cols=[c for c in {v for r in g for v in r} if c!=bg]
    def box(c):
        P=[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v==c]
        xs,ys=zip(*P)
        t=min(xs);b=max(xs);l=min(ys);r=max(ys)
        return t,b,l,r,(b-t+1)*(r-l+1)==len(P),P
    B={c:box(c)for c in cols}
    rc=[c for c,v in B.items() if v[4]][0]
    mc=[c for c in cols if c!=rc][0]
    rect=set()
    for i,j in B[mc][5]:
        L=g[i][j-1] if j>0 else bg;R=g[i][j+1] if j<w-1 else bg
        U=g[i-1][j] if i>0 else bg;D=g[i+1][j] if i<h-1 else bg
        if (L==bg and R==bg) or (U==bg and D==bg):
            continue
        rect.add((i,j))
    st=min(i for i,j in rect);sb=max(i for i,j in rect)
    sl=min(j for i,j in rect);sr=max(j for i,j in rect)
    dt,db,dl,dr=B[rc][:4]
    if sl<=dr and dl<=sr:
        di=db+1-st if st>db else dt-1-sb;dj=0
    else:
        dj=dr+1-sl if sl>dr else dl-1-sr;di=0
    res=[[bg if v==mc else v for v in r] for r in g]
    for i,j in rect:res[i+di][j+dj]=mc
    return res
