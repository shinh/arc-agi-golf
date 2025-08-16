def p(g):
    # extend the lone colored cell toward its neighbor
    h=len(g);w=len(g[0]);f=sum(g,[]);c=min(f,key=f.count);y,x=divmod(f.index(c),w)
    for a,b in((0,1),(1,0),(0,-1),(-1,0)):
        Y,X=y+a,x+b
        if h>Y>=0<=X<w and g[Y][X] and not(h>y-a>=0<=x-b<w and g[y-a][x-b]):
            while h>Y>=0<=X<w:g[Y][X]=g[Y][X] or c;Y+=a;X+=b
            return g
