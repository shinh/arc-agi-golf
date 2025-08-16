def p(g):
    # crop region with most 2s
    v=set();m=-1
    for y,r in enumerate(g):
        for x,c in enumerate(r):
            if c and(y,x)not in v:
                q=[(y,x)];v|={(y,x)};y1=y2=y;x1=x2=x;n=c==2
                while q:
                    i,j=q.pop()
                    for u,w in((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                        if-1<u<20>w>-1 and g[u][w]and(u,w)not in v:
                            v|={(u,w)};q+=[(u,w)];y1=min(y1,u);y2=max(y2,u);x1=min(x1,w);x2=max(x2,w);n+=g[u][w]==2
                if n>m:m=n;B=y1,y2,x1,x2
    y1,y2,x1,x2=B;return[r[x1:x2+1]for r in g[y1:y2+1]]
