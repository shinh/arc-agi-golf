def p(g):
    # copy and solve
    h,w=len(g),len(g[0]);o=[r[:]for r in g]
    for i in range(h):
        for j in range(w):
            if g[i][j]==9:
                q=[(i,j)];g[i][j]=1
                a=b=i;c=d=j
                while q:
                    x,y=q.pop();a=min(a,x);b=max(b,x);c=min(c,y);d=max(d,y)
                    for k in range(x+1,h):o[k][y]=o[k][y]or 1
                    for u in x-1,x,x+1:
                        for v in y-1,y,y+1:
                            if 0<=u<h and 0<=v<w and g[u][v]==9:g[u][v]=1;q+=[(u,v)]
                n=(d-c+1)//2
                for u in range(max(0,a-n),min(h,b+n+1)):
                    for v in range(max(0,c-n),min(w,d+n+1)):
                        if g[u][v]==0:o[u][v]=3
    return o
