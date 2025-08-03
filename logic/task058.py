def p(g):
    n=len(g);o=create(n,n);x=y=0;o[0][0]=3
    d=0;l=n;m=n-1;f=1
    dx=1,0,-1,0;dy=0,1,0,-1
    while 1:
        for _ in range(l-1 if f else l):
            x+=dx[d];y+=dy[d];o[y][x]=3
        f=0;d=(d+1)%4
        if m<1:break
        for _ in range(m):
            x+=dx[d];y+=dy[d];o[y][x]=3
        d=(d+1)%4;l=m;m-=2
        if l<1:break
    return o
