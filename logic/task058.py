def p(g):# draw spiral of 3s
    n=len(g);o=create(n,n);x=y=d=0;l=m=n-1;o[0][0]=3;D=1,0,-1,0
    while l>0:
        for s in(l,m):
            for _ in[0]*s:x+=D[d];y+=D[d-1];o[y][x]=3
            d=-~d&3
        l,m=m,m-2
    return o
