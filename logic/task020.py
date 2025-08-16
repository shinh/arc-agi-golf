def p(g):
    # rotate points around their box center
    P=[(y,x,v)for y,r in enumerate(g)for x,v in enumerate(r)if v]
    if not P:return g
    ys,xs,_=zip(*P);b,d=min(ys),max(ys);a,c=min(xs),max(xs);cx=(a+c)/2;cy=(b+d)/2
    o=[[0]*10 for _ in g]
    for y,x,v in P:
        x-=cx;y-=cy
        o[int(round(y+cy))][int(round(x+cx))]=v;x,y=y,-x
        o[int(round(y+cy))][int(round(x+cx))]=v;x,y=y,-x
        o[int(round(y+cy))][int(round(x+cx))]=v;x,y=y,-x
        o[int(round(y+cy))][int(round(x+cx))]=v;x,y=y,-x
    return o

