def p(g):
    h=len(g);w=len(g[0])
    R=[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v==4]
    if len(R)-4:return g
    a=min(i for i,_ in R);b=max(i for i,_ in R);c=min(j for _,j in R);d=max(j for _,j in R)
    di={};I=[]
    for i in range(a+1,b):
        for j in range(c+1,d):
            if(v:=g[i][j]):di[v]=di.get(v,0)+1;I.append((i,j))
    do={};O=[]
    for i in range(h):
        for j in range(w):
            if not(a<=i<=b and c<=j<=d)and(v:=g[i][j]):do[v]=do.get(v,0)+1;O.append((i,j))
    if not(I and O):return [r[c:d+1]for r in g[a:b+1]]
    mA=min(i for i,_ in O);nA=max(i for i,_ in O);oA=min(j for _,j in O);pA=max(j for _,j in O)
    E=min(i for i,_ in I);K=min(j for _,j in I)
    cols=list(di);r=[di[c]//do.get(c,1)for c in cols];mc=max(set(r),key=r.count)
    sel=[c for c,t in zip(cols,r)if t==mc]
    Is=[(i,j)for i,j in I if g[i][j]in sel];Os=[(i,j)for i,j in O if g[i][j]in sel]
    e=min(i for i,_ in Is);f=max(i for i,_ in Is);k=min(j for _,j in Is);l=max(j for _,j in Is)
    m=min(i for i,_ in Os);n=max(i for i,_ in Os);o=min(j for _,j in Os);p=max(j for _,j in Os)
    hr=(l-k+1)//(p-o+1);vr=(f-e+1)//(n-m+1)
    P=[g[i][oA:pA+1]for i in range(mA,nA+1)]
    U=[[v for v in r for _ in range(hr)]for r in P for _ in range(vr)]
    S=[(i,j,v)for i,r in enumerate(U)for j,v in enumerate(r)if v]
    uE=min(i for i,j,v in S if v in sel);uK=min(j for i,j,v in S if v in sel)
    sh=E-uE;sk=K-uK
    G=[r[:]for r in g]
    for i,j,v in S:
        ii=i+sh;jj=j+sk
        if 0<=ii<h and 0<=jj<w:G[ii][jj]=v
    return [r[c:d+1]for r in G[a:b+1]]
