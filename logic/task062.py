def p(g):
    o=[[3]*10 for _ in g];C=[(y,x)for y,r in enumerate(g)for x,v in enumerate(r)if v not in (0,2)];T=[(y,x)for y,r in enumerate(g)for x,v in enumerate(r)if v==2];c=g[C[0][0]][C[0][1]]
    xc=[x for y,x in C];xt=[x for y,x in T]
    if min(xt)>max(xc) or max(xt)<min(xc):a=min(xt)+max(xc) if min(xt)>max(xc) else max(xt)+min(xc);f=lambda y,x:(y,a-x)
    else:yc=[y for y,x in C];yt=[y for y,x in T];a=min(yt)+max(yc) if min(yt)>max(yc) else max(yt)+min(yc);f=lambda y,x:(a-y,x)
    for y,x in C:y2,x2=f(y,x);o[y][x]=o[y2][x2]=c
    return o
