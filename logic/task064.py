def p(g):
    t=[[]for _ in range(10)]
    for y,r in enumerate(g):
        for x,v in enumerate(r):t[v]+=((y,x),)
    m=-1
    for k,v in enumerate(t):
        if v:
            ys=[y for y,_ in v];xs=[x for _,x in v]
            a=min(ys);b=max(ys);c=min(xs);d=max(xs);n=len(v)
            if (b-a+1)*(d-c+1)==n>m:m=n;rc=k;R=(a,b,c,d)
    rare=min((len(v),k)for k,v in enumerate(t)if k!=rc and v)[1]
    o=[r[:]for r in g];a,b,c,d=R
    for y,x in t[rare]:
        if c<=x<=d:
            for i in(range(y,a)if y<a else range(b+1,y+1)):o[i][x]=rare
        elif a<=y<=b:
            for j in(range(x,c)if x<c else range(d+1,x+1)):o[y][j]=rare
    return o

