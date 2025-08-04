def p(g):
    h=len(g);w=len(g[0])
    R=[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v==4]
    if len(R)!=4:return g
    a=min(i for i,_ in R);b=max(i for i,_ in R);c=min(j for _,j in R);d=max(j for _,j in R)
    di={};I=[]
    for i in range(a+1,b):
        for j in range(c+1,d):
            v=g[i][j]
            if v:di[v]=di.get(v,0)+1;I.append((i,j))
    do={};O=[]
    for i in range(h):
        for j in range(w):
            if not(a<=i<=b and c<=j<=d):
                v=g[i][j]
                if v:do[v]=do.get(v,0)+1;O.append((i,j))
    if not I or not O:return [row[c:d+1]for row in g[a:b+1]]
    E=min(i for i,_ in I);K=min(j for _,j in I)
    mA=min(i for i,j in O);nA=max(i for i,j in O);oA=min(j for i,j in O);pA=max(j for i,j in O)
    cols=list(di);r=[di[c]//do.get(c,1) for c in cols];mc=max(set(r),key=r.count)
    sel=[c for c,t in zip(cols,r) if t==mc]
    Is=[(i,j)for i,j in I if g[i][j] in sel];Os=[(i,j)for i,j in O if g[i][j] in sel]
    e=min(i for i,_ in Is);f=max(i for i,_ in Is);k=min(j for _,j in Is);l=max(j for _,j in Is)
    m=min(i for i,_ in Os);n=max(i for i,_ in Os);o=min(j for _,j in Os);p=max(j for _,j in Os)
    hr=(l-k+1)//(p-o+1);vr=(f-e+1)//(n-m+1)
    P=[g[i][oA:pA+1]for i in range(mA,nA+1)]
    U=[[v for v in r for _ in range(hr)]for r in P for _ in range(vr)]
    G=[r[:]for r in g]
    for i,r in enumerate(U):
        ii=E+i
        if ii<h:
            row=G[ii]
            for j,v in enumerate(r):
                jj=K+j
                if jj<w and v:row[jj]=v
    return [row[c:d+1]for row in G[a:b+1]]
