def p(g):
    h=len(g);w=len(g[0])
    for c in range(1,10):# move tiles toward full row/column else erase
        z=[*zip(*g)];r=k=-1
        if (t:=[c]*w)in g:r=g.index(t)
        elif (t:=(c,)*h)in z:k=z.index(t)
        for y in range(h):
            for x in range(w):
                if g[y][x]==c:
                    if ~r and y-r:g[y][x]=0;g[r+(y>r)-(y<r)][x]=c
                    elif ~k and x-k:g[y][x]=0;g[y][k+(x>k)-(x<k)]=c
                    elif r<0>k:g[y][x]=0
    return g
