def p(g):
    a=[]
    for k in range(8):
        r=g[k]
        c=max(r,key=r.count)
        for i in range(2):
            if r[i]==r[6+i]and r[i]!=c:a+=[k,3+i,r[i]],
            if g[i][k]==g[6+i][k]and g[i][k]!=c:a+=[3+i,k,g[i][k]],
    for y,x,c in a:
        g[y][x]=c
    return g
