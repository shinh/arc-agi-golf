def p(g):
    # drop 1s below 9s and surround with 3
    o=[r[:]for r in g];h=len(g);w=len(g[0]);R=range
    for i,r in enumerate(g):
        for j,v in enumerate(r):
            if v>8:
                q=[(i,j)];r[j]=1;a=b=i;c=d=j
                for x,y in q:
                    a,b,c,d=min(a,x),max(b,x),min(c,y),max(d,y)
                    for t in o[x+1:]:t[y]+=t[y]<1
                    for u in R(x-1,x+2):
                        for v in R(y-1,y+2):
                            if h>u>=0<=v<w and g[u][v]>8:g[u][v]=1;q+=(u,v),
                n=d-c+1>>1
                for u in R(a-n,b+n+1):
                    for v in R(c-n,d+n+1):
                        if h>u>=0<=v<w and g[u][v]<1:o[u][v]=3
    return o
