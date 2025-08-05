def p(g):
    h=len(g);w=len(g[0]);R=[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v==4]
    if len(R)-4:return g
    x,y=zip(*R);a=min(x);b=max(x);c=min(y);d=max(y)
    di={};I=[(i,j)for i in range(a+1,b)for j in range(c+1,d)if(v:=g[i][j])and(di.update({v:di.get(v,0)+1})or 1)]
    do={};O=[(i,j)for i in range(h)for j in range(w)if(i<a or i>b or j<c or j>d)and(v:=g[i][j])and(do.update({v:do.get(v,0)+1})or 1)]
    if not(I and O):return[r[c:d+1]for r in g[a:b+1]]
    x,y=zip(*O);A=min(x);B=max(x);C=min(y);D=max(y)
    cols=[c for c in di if c in do];r=[di[c]//do[c]for c in cols];mc=max(set(r),key=r.count)
    sel=[c for c,t in zip(cols,r)if t==mc]
    Is=[(i,j)for i,j in I if g[i][j]in sel];Os=[(i,j)for i,j in O if g[i][j]in sel]
    x,y=zip(*Is);e=min(x);f=max(x);k=min(y);l=max(y)
    x,y=zip(*Os);m=min(x);n=max(x);o=min(y);p=max(y)
    H=(l-k+1)//(p-o+1);V=(f-e+1)//(n-m+1)
    P=[g[i][C:D+1]for i in range(A,B+1)]
    U=[[v for v in r for _ in range(H)]for r in P for _ in range(V)]
    S=[(i,j,v)for i,r in enumerate(U)for j,v in enumerate(r)if v]
    u=min(i for i,j,v in S if v in sel);v0=min(j for i,j,v in S if v in sel)
    sh=e-u;sk=k-v0;G=[r[:]for r in g]
    for i,j,v in S:
        ii=i+sh;jj=j+sk
        if 0<=ii<h and 0<=jj<w:G[ii][jj]=v
    return[r[c:d+1]for r in G[a:b+1]]
