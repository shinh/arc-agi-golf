def p(g):
    # extend the lone colored cell toward its neighbor
    h=len(g);w=len(g[0]);f=sum(g,[]);c=min(f,key=f.count);y,x=divmod(f.index(c),w)
    a=(g[y+1][x]>0)-(g[y-1][x]>0)
    b=(g[y][x+1]>0)-(g[y][x-1]>0)
    while 0<=y+a<h and 0<=x+b<w:
        y+=a;x+=b;g[y][x]=g[y][x] or c
    return g
