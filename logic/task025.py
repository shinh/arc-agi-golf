def p(g):
    h=len(g);w=len(g[0])
    for c in range(1,10):# move tiles toward full row/column else erase
        z=[*zip(*g)];r=k=-1
        if [c]*w in g:r=g.index([c]*w)
        elif (c,)*h in z:k=z.index((c,)*h)
        for i in range(h*w):
            y,x=divmod(i,w)
            if g[y][x]==c:
                if r+1 and y!=r:g[y][x]=0;g[r+(y>r)-(y<r)][x]=c
                elif k+1 and x!=k:g[y][x]=0;g[y][k+(x>k)-(x<k)]=c
                elif r==k<0:g[y][x]=0
    return g
