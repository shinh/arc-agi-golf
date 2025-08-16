def p(g):
    # expand rare color rectangle outward
    h=len(g);w=len(g[0]);a=sum(g,[]);c=min({*a},key=a.count)
    Y,X=zip(*[(i//w,i%w)for i in range(h*w)if a[i]==c]);t=min(Y);b=max(Y);l=min(X);r=max(X)
    d=b-t+1>>1;e=r-l+1>>1
    for _ in[0]*13:
        for y in t,b:
            if 0<=y<h:
                for x in range(l,r+1):
                    if 0<=x<w:g[y][x]=c
        for x in l,r:
            if 0<=x<w:
                for y in range(t,b+1):
                    if 0<=y<h:g[y][x]=c
        t-=d;l-=e;b+=d;r+=e
    return g
