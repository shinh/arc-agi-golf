def p(g):
    # link every 8 to the side wall then duplicate its row
    H=len(g);W=len(g[0]);R=range
    P=[(y,x)for y in R(H)for x in R(W)if g[y][x]==2]
    E=[(y,x)for y in R(H)for x in R(W)if g[y][x]==8]
    lc=min(x for y,x in P);rc=max(x for y,x in P)
    sc,st,ot=[(lc,min(y for y,x in P if x==lc),min(y for y,x in P if x==rc)),(rc,min(y for y,x in P if x==rc),min(y for y,x in P if x==lc))][not any(g[y][lc]==2 or x==lc for y,x in E)]
    for y,x in E:
        a,b=sorted((sc,x))
        g[y][a+1:b]=[8]*(b-a-1);g[y][x]=4;r=y+ot-st
        if 0<=r<H:g[r]=[8]*W
    for y,x in P:g[y][x]=2
    return g
