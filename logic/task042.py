def p(g):
    h=len(g);w=len(g[0])
    s=[(y,x)for y in range(h)for x in range(w)if g[y][x]==3]
    v={}
    for i,(y,x) in enumerate(s):
        for Y,X in s[i+1:]:
            dy=Y-y;dx=X-x
            if abs(dy)==abs(dx):
                v[(dy,dx)]=v.get((dy,dx),0)+1
                v[(-dy,-dx)]=v.get((-dy,-dx),0)+1
    for i,(y,x) in enumerate(s):
        for Y,X in s[i+1:]:
            dy=Y-y;dx=X-x
            if (D:=abs(dy))==abs(dx) and v[(dy,dx)]==D*D:
                for A,B in((2*y-Y,2*X-x),(2*Y-y,2*x-X)):
                    if 0<=A<h and 0<=B<w and g[A][B]==0:g[A][B]=8
    return g
