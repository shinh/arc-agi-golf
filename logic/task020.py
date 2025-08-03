def p(g):
    a=b=9;c=d=0
    for y,r in enumerate(g):
        for x,v in enumerate(r):
            if v:a=min(a,x);c=max(c,x);b=min(b,y);d=max(d,y)
    x=(a+c)//2;y=(b+d)//2
    for i in range(y):
        r=g[i]
        for k in range(a,x):
            l=x*2-k;v=r[k];w=r[l]
            if v*w==0:r[k]=r[l]=v or w
        g[y*2-i]=r[:]
    u=g[b][x];r=g[y]
    for k in range(a,c+1):
        if g[b][k] and k!=x and r[k]==0:r[k]=u
    return g
