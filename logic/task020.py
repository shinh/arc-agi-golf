def p(g):
    w=h=10;pts=[(y,x,g[y][x])for y in range(h)for x in range(w)if g[y][x]]
    if not pts:return g
    ys=[y for y,_,_ in pts];xs=[x for _,x,_ in pts];b,d=min(ys),max(ys);a,c=min(xs),max(xs)
    cx=(a+c)/2;cy=(b+d)/2
    o=[[0]*w for _ in range(h)]
    for y,x,v in pts:
        xx=x-cx;yy=y-cy
        for Y,X in((y,x),(cy+xx,cx-yy),(2*cy-y,2*cx-x),(cy-xx,cx+yy)):
            Y=int(round(Y));X=int(round(X))
            if 0<=Y<h and 0<=X<w:o[Y][X]=v
    return o

