def p(g):
    H=19;W=8
    P=[(y,x)for y in range(H)for x in range(W)if g[y][x]==2]
    E=[(y,x)for y in range(H)for x in range(W)if g[y][x]==8]
    lc=min(x for _,x in P);rc=max(x for _,x in P)
    L=[y for y,x in P if x==lc];R=[y for y,x in P if x==rc]
    if any(y in L or x==lc for y,x in E):sc,st,ot=lc,min(L),min(R)
    else:sc,st,ot=rc,min(R),min(L)
    d=ot-st
    for y,x in E:
        if x>sc:a,b=sc+1,x
        else:a,b=x+1,sc
        for j in range(a,b):g[y][j]=8
        g[y][x]=4;r=y+d
        if 0<=r<H:
            for j in range(W):g[r][j]=8
    for y,x in P:g[y][x]=2
    return g
