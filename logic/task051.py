def p(g):
    # extend the lone colored cell toward its neighbor
    f=sum(g,[]);w=len(g[0]);i=f.index(c:=min(f,key=f.count));x=i%w;y=i//w;b,a=[(f[i+o]>0)-(f[i-o]>0)for o in(1,w)]
    while len(g)>(y:=y+a)>-1<(x:=x+b)<w:g[y][x]=g[y][x]or c
    return g
