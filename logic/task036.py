def p(g):
    d={}
    for y,r in enumerate(g):
        for x,v in enumerate(r):
            if v:
                t=d.setdefault(v,[0,99,99,0,0]);t[0]+=1;t[1]=min(t[1],y);t[2]=min(t[2],x);t[3]=max(t[3],y);t[4]=max(t[4],x)
    m=1e9
    for k,(n,y0,x0,y1,x1) in d.items():
        if all(g[y][x] in (0,k) for y in range(y0,y1+1) for x in range(x0,x1+1)) and n<m:
            m=n;best=(k,y0,x0,y1,x1)
    k,y0,x0,y1,x1=best
    return [[k*(g[y][x]==k)for x in range(x0,x1+1)]for y in range(y0,y1+1)]
