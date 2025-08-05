def p(g):
    w=h=r=c=6
    for y in range(h):
        for x in range(w):
            if g[y][x]:r=min(r,y);c=min(c,x)
    a,b,e,d=g[r][c],g[r][c+1],g[r+1][c],g[r+1][c+1]
    L=min(2,c);R=min(2,w-c-2);T=min(2,r);B=min(2,h-r-2)
    for i in range(T):
        t=g[r-1-i];t[c-L:c]=[d]*L;t[c+2:c+2+R]=[e]*R
    for i in range(B):
        t=g[r+2+i];t[c-L:c]=[b]*L;t[c+2:c+2+R]=[a]*R
    return g
