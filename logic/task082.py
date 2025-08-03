def p(g):
    r=g[0];m=len(r);s=[0]*m
    for i,v in enumerate(r):
        if v:
            if i:s[i-1]=v
            if i<m-1:s[i+1]=v
    return [(r,s)[i%2][:] for i in range(len(g))]
