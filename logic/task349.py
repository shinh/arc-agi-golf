def p(g):
    # drop 1s below 9s and surround with 3
    h=len(g);w=len(g[0]);o=[r[:]for r in g]
    for i in range(h):
        for j in range(w):
            if g[i][j]>8:
                q=[(i,j)];g[i][j]=1;a=b=i;c=d=j
                for x,y in q:
                    a,b,c,d=min(a,x),max(b,x),min(c,y),max(d,y)
                    for k in range(x+1,h):o[k][y]+=o[k][y]<1
                    for u in range(x-1,x+2):
                        for v in range(y-1,y+2):
                            if h>u>=0<=v<w and g[u][v]>8:g[u][v]=1;q+=(u,v),
                n=d-c+1>>1
                for u in range(max(0,a-n),min(h,b+n+1)):
                    for v in range(max(0,c-n),min(w,d+n+1)):
                        if g[u][v]<1:o[u][v]=3
    return o
