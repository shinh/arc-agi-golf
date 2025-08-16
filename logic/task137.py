def p(g):
    # expand rare color rectangle outward
    h=len(g);w=len(g[0]);a=sum(g,[])
    c=min({*a},key=a.count)
    Y,X=zip(*[(i//w,i%w)for i,v in enumerate(a)if v==c]);t=min(Y);b=max(Y);l=min(X);r=max(X)
    dy=(b-t+1)//2;dx=(r-l+1)//2
    for _ in[0]*30:
        for x in range(max(l,0),min(r,w-1)+1):
            if 0<=t<h:g[t][x]=c
            if 0<=b<h:g[b][x]=c
        for y in range(max(t,0),min(b,h-1)+1):
            if 0<=l<w:g[y][l]=c
            if 0<=r<w:g[y][r]=c
        t-=dy;l-=dx;b+=dy;r+=dx
    return g
