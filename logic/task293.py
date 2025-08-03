def p(g):
    d={}
    for y,r in enumerate(g):
        for x,c in enumerate(r):
            if c:
                if c in d:
                    a=d[c]
                    if y<a[0]:a[0]=y
                    if x<a[1]:a[1]=x
                    if y>a[2]:a[2]=y
                    if x>a[3]:a[3]=x
                else:d[c]=[y,x,y,x]
    vs=[(c,v) for c,v in d.items() if v[2]-v[0]>v[3]-v[1]]
    hs=[(c,v) for c,v in d.items() if v[3]-v[1]>v[2]-v[0]]
    v=max(vs,key=lambda t:t[1][2]-t[1][0])[0]
    h=max(hs,key=lambda t:t[1][3]-t[1][1])[0]
    A,B=d[v],d[h]
    y0=max(A[0],B[0]);y1=min(A[2],B[2])
    x0=max(A[1],B[1]);x1=min(A[3],B[3])
    for y in range(y0,y1+1):
        for x in range(x0,x1+1):g[y][x]=v if g[y][x]==h else h
    return g
