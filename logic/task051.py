def p(g):
    # extend the lone colored cell toward its neighbor
    f=sum(g,[]);w=len(g[0]);i=f.index(c:=min(f,key=f.count));y=i//w;x=i%w;a,b=[(f[i+o]>0)-(f[i-o]>0)for o in(w,1)]
    while-1<(y:=y+a)<len(g)>-1<(x:=x+b)<w:g[y][x]=g[y][x]or c
    return g
