def p(g):
    # find biggest frame and recolor matching shapes
    v=set();o=[];R=range(20)
    for y in R:
        for x in R:
            if g[y][x]and(y,x)not in v:
                c=g[y][x];q=[(y,x)];v.add((y,x))
                for Y,X in q:
                    for a,b in((1,0),(-1,0),(0,1),(0,-1)):
                        u,V=Y+a,X+b
                        if u in R and V in R and g[u][V]==c and(u,V)not in v:v.add((u,V));q+=(u,V),
                o+=q,
    f=[]
    for s in o:
        ys,xs=zip(*s);t=min(ys);b=max(ys);l=min(xs);r=max(xs)
        if len(s)==2*(b-t+r-l):f+=((b-t)*(r-l),t,b,l,r),
    _,t,b,l,r=max(f)
    P=[(y,x)for y in range(t+1,b)for x in range(l+1,r)if g[y][x]]
    y,x=P[0];c=g[y][x]
    ys,xs=zip(*P);a=min(ys);b=min(xs);S={(y-a,x-b)for y,x in P}
    for s in o:
        ys,xs=zip(*s);a=min(ys);b=min(xs)
        if {(y-a,x-b)for y,x in s}==S:
            for y,x in s:g[y][x]=c
    return g
