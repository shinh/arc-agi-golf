def p(g):
    # crop region with most 2s
    R=range(20);h=[r[:]for r in g];m=-1
    for y in R:
        for x in R:
            if h[y][x]:
                q=[(y,x)];h[y][x]=0
                for i,j in q:
                    for u,w in((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                        if-1<u<20>w>-1 and h[u][w]:h[u][w]=0;q+=[(u,w)]
                Y,X=zip(*q);n=sum(g[i][j]==2 for i,j in q)
                if n>m:m=n;B=min(Y),max(Y),min(X),max(X)
    a,b,c,d=B
    return[r[c:d+1]for r in g[a:b+1]]
