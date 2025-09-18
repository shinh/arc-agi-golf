def p(g):
    # rot
    P=[(y,x,v)for y,r in enumerate(g)for x,v in enumerate(r)if v]
    if not P:return g
    ys,xs,_=zip(*P);cx=(min(xs)+max(xs))>>1;cy=(min(ys)+max(ys))>>1
    o=[[0]*10for _ in g]
    for y,x,v in P:
        x-=cx;y-=cy
        o[cy+y][cx+x]=o[cy-x][cx+y]=o[cy-y][cx-x]=o[cy+x][cx-y]=v
    return o

