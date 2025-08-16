def p(g):
    # expand bars from each 2
    h=len(g);w=len(g[0])
    for y,x in[(Y,X)for Y,R in enumerate(g)for X,v in enumerate(R)if v==2]:
        u=d=l=r=0
        while y>u and g[y-u-1][x]:u+=1
        while y+d+1<h and g[y+d+1][x]:d+=1
        while x>l and g[y][x-l-1]:l+=1
        while x+r+1<w and g[y][x+r+1]:r+=1
        n=min(u+d,l+r)
        t=max(0,y-n);B=min(h-1,y+n)
        L=max(0,x-n);R=min(w-1,x+n)
        if not u:t=0
        if not d:B=h-1
        if not l:L=0
        if not r:R=w-1
        for i in range(t,B+1):g[i][L:R+1]=[3]*(R-L+1)
        Y=(d<1)-(u<1);X=(r<1)-(l<1);a,b=y,x
        while 0<=a<h and 0<=b<w:
            if t<=a<=B and L<=b<=R:g[a][b]=2
            a+=Y;b+=X
    return g
