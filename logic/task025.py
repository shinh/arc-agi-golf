def p(g):
    h=len(g);w=len(g[0]);R=range
    for c in R(1,10):# move to row/col else erase
        r=-1
        for y in R(h):
            if g[y]==[c]*w:r=y;break
        k=-1
        for x in R(w):
            for y in R(h):
                if g[y][x]!=c:break
            else:k=x;break
        for y in R(h):
            for x in R(w):
                if g[y][x]==c:
                    if ~r*(y-r):g[y][x]=0;g[r+(y>r)-(y<r)][x]=c
                    elif ~k*(x-k):g[y][x]=0;g[y][k+(x>k)-(x<k)]=c
                    elif r<0>k:g[y][x]=0
    return g
