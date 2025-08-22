def p(g):
    # extend the lone colored cell toward its neighbor
    w=len(g[0]);f=sum(g,[]);y,x=divmod(f.index(c:=min(f,key=f.count)),w);a,b=(g[y+1][x]>0)-(g[y-1][x]>0),(g[y][x+1]>0)-(g[y][x-1]>0)
    while len(g)>y+a>-1<x+b<w:
        y+=a;x+=b;g[y][x]=g[y][x]or c
    return g
