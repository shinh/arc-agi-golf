def p(g):
    h=len(g);w=len(g[0]);o=[r[:] for r in g];C=[]
    for y in range(h):
        for x in range(w):
            if g[y][x]==5:
                q=[(y,x)];g[y][x]=0;c=[]
                while q:
                    i,j=q.pop();o[i][j]=0;c.append((i,j))
                    for u,v in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
                        if 0<=u<h and 0<=v<w and g[u][v]==5:
                            g[u][v]=0;q.append((u,v))
                C.append(c)
    C.sort(key=len,reverse=True)
    for c in C:
        a=min(y for y,_ in c);b=min(x for _,x in c)
        H=max(y for y,_ in c)-a+1;W=max(x for _,x in c)-b+1
        t=[(y-a,x-b)for y,x in c];Y=h;X=0
        for x in range(w-W+1):
            y=h-H
            while y and all(o[y+dy-1][x+dx]==0 for dy,dx in t):y-=1
            if y<Y:Y,X=y,x
        for dy,dx in t:o[Y+dy][X+dx]=1
    return o
