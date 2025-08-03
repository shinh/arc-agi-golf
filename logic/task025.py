def p(g):
    h=len(g);w=len(g[0])
    for c in range(1,10):
        r=next((i for i in range(h) if g[i]==[c]*w),-1)
        if r>-1:
            for i in range(h*w):
                y,x=divmod(i,w)
                if g[y][x]==c and y!=r:g[y][x]=0;g[r+(y>r)-(y<r)][x]=c
            continue
        k=next((i for i in range(w) if [g[j][i] for j in range(h)]==[c]*h),-1)
        if k>-1:
            for i in range(h*w):
                y,x=divmod(i,w)
                if g[y][x]==c and x!=k:g[y][x]=0;g[y][k+(x>k)-(x<k)]=c
            continue
        for i in range(h*w):
            y,x=divmod(i,w)
            if g[y][x]==c:g[y][x]=0
    return g
