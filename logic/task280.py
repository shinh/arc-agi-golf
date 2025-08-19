def p(g):
    # expand bars from each 2
    h=len(g);w=len(g[0])
    for y,x in[(y,x)for y in range(h)for x in range(w)if g[y][x]==2]:
        u=d=l=r=0
        while y>u and g[y-u-1][x]:u+=1
        while y+d+1<h and g[y+d+1][x]:d+=1
        while x>l and g[y][x-l-1]:l+=1
        while x+r+1<w and g[y][x+r+1]:r+=1
        n=min(u+d,l+r)
        t=u and max(0,y-n);B=d and min(h-1,y+n) or h-1
        L=l and max(0,x-n);R=r and min(w-1,x+n) or w-1
        for q in g[t:B+1]:q[L:R+1]=[3]*-~(R-L)
        Y=(d<1)-(u<1);X=(r<1)-(l<1);a,b=y,x
        while Y|X and 0<=a<h and 0<=b<w:
            if t<=a<=B and L<=b<=R:g[a][b]=2;a+=Y;b+=X
    return g
